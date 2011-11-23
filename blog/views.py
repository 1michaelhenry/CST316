# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from CST316.blog.models import posts

def home(request):
        entries = posts.objects.all()[:10:-1]
        return render_to_response('index.html', {'posts' : entries }, \
			context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html', \
			context_instance=RequestContext(request))

def auth(request):
	entries = posts.objects.all()[:10:-1]
	return render_to_response('auth.html', {'posts' : entries })

def test(request):
	return render_to_response('test.html', \
			context_instance=RequestContext(request))
