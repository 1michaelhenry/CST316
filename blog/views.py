# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
import datetime
from CST316.blog.models import posts

def getauthblog(request):
	entries = posts.objects.filter(author=request.session['username']).order_by('-timestamp')
	entries = entries[:10]
	return entries

def home(request):
        entries = posts.objects.all()[::-1]
        return render_to_response('index.html', {'posts' : entries }, \
			context_instance=RequestContext(request))

def logout(request):
	del request.session['username']
	return HttpResponseRedirect('/')

def loginerror(request):
	return render_to_response(
		'loginerror.html',
		context_instance=RequestContext(request))

def authorize(request):
	if 'username' not in request.POST:
		return HttpResponseRedirect('loginerror')
	user = auth.authenticate(
		username=request.POST['username'],
                password=request.POST['password'])
        if user is not None:
                request.session['username'] = request.POST['username']
                entries = getauthblog(request)
                return render_to_response(
                        'auth.html',
                        {'posts':entries,
                         'user' :request.session['username']},
                        context_instance=RequestContext(request))
        else:
                return HttpResponseRedirect('/loginerror')

def postblog(request):
	post = posts(
		author=request.session['username'],
		title=request.POST['title'],
		bodytext=request.POST['bodytext'],
		timestamp=datetime.datetime.now())
	post.save()
	entries = getauthblog(request)
	return render_to_response(
		'auth.html',
		{'posts' : entries,
		'user':request.session['username']},
		context_instance=RequestContext(request))

def previewblog(request):
	post = posts(
		author=request.session['username'],
		title=request.POST['title'],
		bodytext=request.POST['bodytext'],
		timestamp=datetime.datetime.now())
	entries = getauthblog(request)
	return render_to_response(
		'preview.html',
		{'newpost': post,
		 'posts' : entries,
		 'user' : request.session['username']},
		 context_instance=RequestContext(request))

def cancelpost(request):
	entries = getauthblog(request)
	return render_to_response(
		'auth.html',
		{'posts':entries,
		 'user' :request.session['username']},
		context_instance=RequestContext(request))
