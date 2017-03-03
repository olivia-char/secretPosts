from django.shortcuts import render, redirect, HttpResponse
from .models import User, Secret
from django.contrib import messages
from django.db.models import Count

# Create your views here.

def index(request):
	# if id not in request.session:
	# 	request.session['id'] = -1
	print "first page"
	return render(request, 'secrets/index.html')

def register(request):
	print "register page"
	if request.method == 'POST':
		fname = request.POST['first_name']
		lname = request.POST['last_name']
		email = request.POST['email']
		pw = request.POST['password']
		cpw = request.POST['c_password']

	newUser = User.userManager.register(fname, lname, email, pw, cpw) 
	print "sent to db"

	if newUser[0] == False:
		print newUser[1]['errorMessage']
		errorMessage = newUser[1]['errorMessage']
		for i in errorMessage:
			messages.error(request, i)
		return redirect('/')
	else:
		request.session['id'] = newUser[1].id
		print newUser[1].id	
		return redirect("/homepage")

def login(request):
	print "login page"
	if request.method == 'POST':
 		email = request.POST.get('email')
		password = request.POST.get('password')
		loginUser = User.userManager.login(email, password)

		if loginUser[0] == False:
			errorMessage = loginUser[1]['errorMessage']
			for i in errorMessage:
				messages.error(request, i)
			return redirect('/') 
		else:
			print loginUser[1]
			request.session['id'] = loginUser[1].id 
			print "What's in session", request.session['id']
		
		return redirect('/homepage') 

def homepage(request):
	if 'id' not in request.session:
		messages.error(request, 'must sign in')
		return redirect('/') 
	else:
		print "success!"
		context = {
			'newSecrets': Secret.secretManager.all().order_by('-created_at')[0:10],
			'users': User.userManager.get(id=request.session['id']),
		}
		return render(request, 'secrets/homepage.html', context)

def create(request):
	print "create"
	if request.method == 'POST':
		secretPost = Secret.secretManager.addSecret(secret=request.POST['secret'], id=request.session['id'])
		
		if secretPost[0] == False:
			errorMessage = secretPost[1]['errorMessage']
			for i in errorMessage:
				messages.error(request, i) 
			return redirect('/homepage')
	 
	return redirect('/homepage')

def like(request):
	if request.method == 'POST':
		like_id = request.POST['like']
		secret_object = Secret.secretManager.get(id=like_id)
		user_object = User.userManager.get(id=request.session['id'])
		secret_object.like.add(user_object)
		
		# like = Secret.secretManager.create(like=request.POST['like'], id=request.session['id'])
	print "like"
	return redirect('/homepage')

def popular(request):
	context ={
		'popSecrets': Secret.secretManager.all().annotate(num_like=Count('like')).order_by('-num_like'),
		'users': User.userManager.get(id=request.session['id']),
	}
	return render(request, 'secrets/popular.html', context)

def likePop(request):
	if request.method == 'POST':
		like_id = request.POST['like']
		secret_object = Secret.secretManager.get(id=like_id)
		user_object = User.userManager.get(user_id=request.session['id'])
		secret_object.like.add(user_object)
		
		# like = Secret.secretManager.create(like=request.POST['like'], id=request.session['id'])
	print "like"
	return redirect('/popular')

def delete(request):
	if request.method == 'POST':
		delete_id = request.POST['delete']
		secret_object = Secret.secretManager.get(id=delete_id)
		user_object = User.userManager.get(id=request.session['id'])
		secret_object.delete() 
	return redirect('/homepage')

def mine(request):
	context = {
		'mySecrets': Secret.secretManager.filter(user=request.session['id'])
	}
	return render(request, 'secrets/mine.html', context)

def logout(request):
	if request.method == 'POST':
		# logout_id = request.POST['logout']
		# user_object = User.userManager.get(id=request.session['id'])
		# user_object.delete()
		request.session.pop('id')
	return redirect('/')









