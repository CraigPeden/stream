from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import View, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from web.forms import StreamForm
from web.models import Stream
from django.db.models.query import *
from django.contrib.auth.decorators import login_required
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

		if form.is_valid():
			username = form.clean_username()
			password = form.clean_password2()
			user = form.save()
			Stream.objects.create(user=user)
			instance = authenticate(username=username, password=password)
			login(request,instance)
			return redirect('/')

		return render_to_response('registration/register.html',{'form': form},RequestContext(request))
		
class account(UpdateView):
	model = User
	form = UserChangeForm
		
class profile(UpdateView):
	model = Stream
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			stream = get_object_or_404(Stream, user=request.user)
			return render_to_response('app/stream_form.html',{'form': StreamForm(instance=stream)},RequestContext(request))
		else:
			redirect('/login/')
		
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			stream = get_object_or_404(Stream, user=request.user)
			if request.user != stream.user:
				return redirect('noEntry')
			else:  
				form = StreamForm(data=request.POST, instance=stream)
				if form.is_valid():
					form.save()
					return redirect('/' + request.user.username)
				else:
					return redirect('error')
		else:
			redirect('/login/')

class stream(View):
	model = Stream
	
	def get(self, request, broadcaster_username):
		broadcaster = Stream.objects.filter(user__username__iexact=broadcaster_username)[0]
		
		return render(request,'app/stream.html',{'broadcaster': broadcaster})
