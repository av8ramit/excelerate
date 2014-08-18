from models import Student, MyUserManager

from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import re



def home(request):
	return render(request, 'userauth/login.html')

def register(request):
	return render(request, 'userauth/register_site.html')

def send(request):

	u_name = p_word = ''
	if request.POST:
		c = {}
		c.update(csrf(request))
		u_name = request.POST.get('username')
		p_word = request.POST.get('password')
		re_pass = request.POST.get('retypepassword')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		school = request.POST.get('school')
		email = request.POST.get('email')
		studentid = request.POST.get('studentid')

		# if not p_word == re_pass:
		# 	error_message = "Passwords do not match"
		# 	context = #whatevs
		# regex = re.compile(".+?@.+?\..+")
		# if not regex.search(email):
		# 	error_message = "Incorrect Email Format"
		# 	context = #bitchs
		# if not studentid.isdigit():
		# 	error_message = "Please put a valid student id"
		# 	context = #peace

		user = Student.objects.create_user(username=u_name, password=p_word,
									first_name=fname, last_name=lname,
									school_name=school, email=email,
									student_id=studentid)
		user.save()
		return HttpResponse("Thank you for registering!")
	else:
		return HttpResponse("Sorry something went wrong")

def login(request):
	u_name = p_word = ''
	if request.POST:
		u_name = request.POST.get('username')
		p_word = request.POST.get('password')
		# print u_name
		# print p_word
		remember = request.POST.get('remember-me', False)
		user = authenticate(username=u_name, password=p_word)
		if user is not None:
			# the password verified
			if user.is_active:
				# Change later
				#login(request, user)
				school = user.school_name
				# return HttpResponse(u_name + " from " + school + " succesfully logged in!")
				return render(request, 'userauth/userpage.html', {'user':user})
			else:
				# User account has been disabled
				return HttpResponse("Sorry, user has been disabled")
		else:
			# Username and password combination was not verified
			return HttpResponse("Username and password incorrect")