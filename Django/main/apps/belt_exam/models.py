from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
	def validator(self, postDATA):
		errors = {}
		if len(postDATA['first_name']) < 2:
			errors["first_name"] = "first name should be at least 2 characters"
		if len(postDATA['last_name']) < 2:
			errors["last_name"] = "last name should be at least 2 characters"
		email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not email_re.match(postDATA['email']):
			errors['email'] = 'Must be a valid email address'
		if User.objects.filter(email=postDATA['email']):
			errors['email'] = 'email already registered with another account'

		passStrength = 0
		passErrors = []
		password = postDATA['password']
		if (len(password) >= 8): #tests if password is at least of length 8
			passStrength += 1
		else:
			passErrors.append('Password should be at least 8 characters long!')

		if (re.compile(r'.*[A-Z].*[A-Z]').match(password)):        #tests for at least 2 capital letters
			passStrength += 1
		else:
			passErrors.append("Password should contain one capital letter")

		if (re.compile(r'.*[!@#$&*]').match(password)):            #tests for at least one special character
			passStrength += 1
		else:
			passErrors.append("Password should contain one special character")

		if (re.compile(r'.*[0-9].*[0-9]').match(password)):        #tests for at least 2 digits
			passStrength += 1
		else:
			passErrors.append("Password should contain at least two digits")

		if (re.compile(r'.*[a-z].*[a-z].*[a-z]').match(password)):    #tests for at least 3 lower case letters
			passStrength += 1
		else:
			passErrors.append("Password should contatin at least 3 lower case letters")

		if passStrength < 3:
			errors['password'] = []
			for error in passErrors:
				errors['password'].append(error)

		if not postDATA['password'] == postDATA['password_confirm']:
			if not 'password' in errors.keys():
				errors['password'] = []
			errors['password'].append('passwords do not match')

		return errors

class JobManager(models.Manager):
	def validator(request, postDATA):
		errors = {}
		if len(postDATA['title']) < 3:
			errors['title'] = 'title must constist of at least 3 characters'
		if len(postDATA['description']) < 3:
			errors['description'] = 'description must contain at least 3 characters'
		if len(postDATA['location']) < 3:
			errors['location'] = 'location must contain at least 3 characters'
		if 'validate_categories' in postDATA:
			if len(postDATA['category_make']) < 1 and 'garden' not in postDATA and 'electrical' not in postDATA and 'pet-care' not in postDATA:
				errors['category'] = 'jobs must have at least one category'
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=3000)
	location = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	author = models.ForeignKey(User, related_name='posted_jobs')
	worker = models.ForeignKey(User, related_name='taken_jobs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = JobManager()

