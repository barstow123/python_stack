from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'index.html')

def login(request):
	user = User.objects.filter(email=request.POST['email'])
	if user:
		if bcrypt.checkpw(request.POST['password'].encode(), user[0].pw_hash.encode()):
			request.session['user_id'] = user[0].id
			return redirect('login_home')
	messages.error(request, 'login_failed', extra_tags='login')
	return redirect('login_index')

def register(request, methods=['POST']):
	errors = User.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('login_index')
	else:
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		request.session['user_id'] = user.id
	return redirect('login_home')

def home(request):
	context = {}
	user = User.objects.get(id=request.session['user_id'])
	context['username'] = f'{user.first_name} {user.last_name}'
	return render(request, 'logged_in.html', context)
