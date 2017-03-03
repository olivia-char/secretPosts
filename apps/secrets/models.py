from __future__ import unicode_literals
from django.db import models 
import re
import time

# Create your models here.

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
	def register(self, first_name, last_name, email, password, c_password):
		
		status = True 
		error = []

		if len(first_name) < 1:
			error.append("First Name Required")
			status = False
		elif len(first_name) <= 2:
			error.append("First Name must be more than 2 characters")
			status = False
		elif not NAME_REGEX.match(first_name):
			error.append("First Name cannot contain numbers")
			status = False
		
		if len(last_name) < 1:
			error.append("Last Name Required")
			status = False
		elif len(last_name) <= 2:
			error.append("Last Name must be more than 2 characters")
			status = False
		elif not NAME_REGEX.match(last_name):
			error.append("Last name cannot contain numbers")
			status = False
		
		if len(email) < 1:
			error.append("Email Required")
			status = False
		elif not EMAIL_REGEX.match(email):
			error.append("Enter a vaild email")
			status = False
		elif len(User.userManager.filter(email=email)) > 0:
			error.append("Email already taken")
			status = False
	
		if len(password) < 1:
			error.append("Password Required")
			status = False
		elif len(password) < 8:
			error.append("Password must be longer than 8 characters")
			status = False
		if password != c_password:
			error.append("Passwords do not match")
			status = False
		
		if status == False:
			return (False, {'errorMessage': error}) 
		if status == True:
			return (True, self.create(first_name=first_name, last_name=last_name, email=email, password=password))

	def login(self, email, password):
		
		status = True 
		error = []

		if len(email) < 1:
			error.append("Email Required")
			status = False

		if len(password) < 1:
			error.append("Password Required")
			status = False

		if status == False:
			return (False, {'errorMessage': error})

		# takes in login email and password looks for existing email and password together
		# user is equal to an array 	
		user = User.userManager.filter(email=email, password=password)
		
		if len(user) > 0:
			print "in the models, got back user", user 
			return (True, user[0]) 
		else:
			error.append("cannot login")
			status = False
			return (False, {'errorMessage': error})

		print email, password 
		
		if status == True:
			return (True, id)
			


class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.EmailField(max_length = 100)
	password = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()

class SecretManager(models.Manager):
	def addSecret(self, id, secret):
		status = True
		error = []	

		if len(secret) < 1:
			error.append("You must enter in a secret") 
			status = False
		
		if status == False:
			return (False, {'errorMessage': error})

		if status == True:
			return (True, self.create(secret=secret, user=User.userManager.get(id=id)))
	
	def likeSecret(self, id):
		print "secret secret"



class Secret(models.Model):
	secret = models.TextField(max_length = 250)
	user = models.ForeignKey(User, related_name='post')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	like = models.ManyToManyField(User, related_name='liked')
	secretManager = SecretManager()









