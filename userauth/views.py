from models import Student, MyUserManager

from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from Library.Console import *
from Library.Values import *

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import re

console = Console()

def home(request):
	"""
	Goes to home page - checks to see if it is sent a post (from postregister page) with the username. If it was, then pre-fill the username field
	"""
	if request.POST:
		c = {}
		c.update(csrf(request))
		u_name = request.POST.get('username')
		return render(request, 'userauth/login.html', { 'username': u_name })
	else:
		return render(request, 'userauth/login.html')

def register(request):
	"""
	Simply sends user to the register page
	"""
	return render(request, 'userauth/register.html')

def send(request):
	"""
	Called after submitting a register form
	Collects all the post information, checks for matching passwords, and does one of two things:
	1. If passwords do not match, reload register form with error message and pre-filled fields
	2. If everything is valid, create user object and send to postregister page with username variable
	""" 
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

		if not p_word == re_pass:
			error_message = "Passwords do not match"
			return render(request, 'userauth/register.html', {
				'username': u_name, 'fname':fname, 'lname':lname, 'school':school, 'email':email, 'studentid':studentid, 'errormsg':error_message
				})
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
		console.process_commands("load_class web")
		console.process_commands("new_student " + u_name)
		return render(request, 'userauth/postregister_base.html', {'username':u_name})
	else:
		return HttpResponse("Sorry something went wrong")

# shouldn't need this - handled in home now
# def postregister(request):
# 	if request.POST:
# 		c = {}
# 		c.update(csrf(request))
# 		u_name = request.POST.get('username')
# 		return render(request, 'userauth/login_post.html', { 'username': u_name })

def login_user(request):
	"""
	Called from login page
	Authenticates username and password
	Loads user page or displays appropriate error
	"""
	u_name = p_word = ''
	if request.POST:
		u_name = request.POST.get('username')
		p_word = request.POST.get('password')
		remember = request.POST.get('remember-me', False)
		user = authenticate(username=u_name, password=p_word)
		if user is not None:
			# adding user cookie getting ERROR when I try to store this cookie
			# request.session['user'] = user 
			# the password verified
			if user.is_active:
				login(request, user) #use this for sessions (built in)
				console.process_commands("load_class web")
				print (console.error)
				console.process_commands("load_student " + u_name)
				print (console.error)
				return render(request, 'userauth/userpage.html', {'user':user})
			else:
				# User account has been disabled
				error_message = "Sorry, this user has been disabled"
				return render(request, 'userauth/login.html', {'errormsg':error_message})
		else:
			# Username and password combination was not verified
			error_message = "Incorrect username or password"
			return render(request, 'userauth/login.html', {'errormsg':error_message})

def formtest2(request):
	"""
	Successfully using the form to input commands as if they were entered through the shell
	"""
	if request.POST:
		context = {}
		context.update(csrf(request))
		cmd = request.POST.get('cmd')
		# try to get the cookie
		# if 'user' in request.session:
		# 	user = request.session['user']
		user = request.user
		print('printing school name')
		print(user.school_name)
		try:
			print (cmd)
			console.process_commands(str(cmd))
			print "hello final"
			if console.error != None:
				response = console.error
			else:
				response = "Successfully called excelerate function: " + cmd
			return render(request, 'userauth/userpage.html', {'response':response, 'user':user})
		except Exception as e:
			response = 'Something went wrong with command:' + cmd + ". Exception outputted: "
			return render(request, 'userauth/userpage.html', {'response':response, 'message':e, 'user':user})
	else:
		response = 'Something wrong with post'
		return render(request, 'userauth/userpage.html', {'response':response, 'user':user})