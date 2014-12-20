from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from models import Stream
from django.db.models.query import *
# Create your views here.

class index(View):
	def get(self, request):
		return render(request,'app/index.html',{})
		
class registerView(View):
	
	def get(self, request, *args, **kwargs):
		form = UserCreationForm()
		return render_to_response('registration/register.html',{'form': form}, RequestContext(request))

	def post(self, request, *args, **kwargs):
		
		form = UserCreationForm(data=request.POST)	
		print form

		if form.is_valid():
			username = form.clean_username()
			password = form.clean_password2()
			user = form.save()
			Stream.objects.create(user=user)
			instance = authenticate(username=username, password=password)
			login(request,instance)
			return redirect('/')

		return render_to_response('registration/register.html',{'form': form},RequestContext(request))


class stream(View):
	
	model = Stream
	
	def get(self, request, broadcaster_username):
		broadcaster = Stream.objects.filter(user__username__iexact=broadcaster_username)[0]
		print broadcaster
		
		return render(request,'app/stream.html',{'broadcaster': broadcaster})
