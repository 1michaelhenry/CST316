# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth

from CST316.blog.models import posts

def getblog(request):
	entries = posts.objects.filter(author=request.POST['author'])
	return entries

def home(request):
        entries = posts.objects.all()[:10:-1]
        return render_to_response('index.html', {'posts' : entries }, \
			context_instance=RequestContext(request))

def logout(request):
	return HttpResponseRedirect('/')

def loginerror(request):
	return render_to_response('loginerror.html', context_instance=RequestContext(request))

def authorize(request):
	user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		request.session['username'] = request.POST['username']
		entries = posts.objects.filter(author=request.session['username'])
		return render_to_response('auth.html', {'posts' : entries, 'user':request.session['username']}, \
		context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/loginerror')

def test(request):
	return render_to_response('test.html', \
			context_instance=RequestContext(request))

def postblog(request):
	post = posts(author=request.session['username'], title=request.POST['title'], bodytext=request.POST['bodytext'])
	post.save()
	entries = posts.objects.filter(author=request.session['username'])[:10:-1]
	return render_to_response('auth.html', {'posts' : entries, 'user':request.session['username']}, \
		context_instance=RequestContext(request))

