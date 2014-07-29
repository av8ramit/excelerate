from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse



def home(request):
	return render(request, 'userauth/login.html')

def register(request):
	u_name = p_word = ''
	if request.POST:
		u_name = request.POST.get('username')
		p_word = request.POST.get('password')
		user = User.objects.create_user(username=u_name, password=p_word)
		user.save()
		return HttpResponse("Thank you for registering!")
	else:
		return HttpResponse("Sorry something went wrong")

def login(request):
	u_name = p_word = ''
	if request.POST:
		u_name = request.POST['username']
		p_word = request.POST['password']
		user = authenticate(username="CHANGEME", password="SECRET")
		if user is not None:
			# the password verified
			if user.is_active:
				# Change later
				login(request, user)
				return HttpResponse(u_name + " succesfully logged in!")
			else:
				# User account has been disabled
				return HttpResponse("Sorry, user has been disabled")
		else:
			# Username and password combination was not verified
			return HttpResponse("Username and password incorrect")