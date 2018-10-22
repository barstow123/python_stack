from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User, Post, Comment
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'log_in.html')

def login(request):
	user = User.objects.filter(email=request.POST['email'])
	if user:
		if bcrypt.checkpw(request.POST['password'].encode(), user[0].pw_hash.encode()):
			request.session['user_id'] = user[0].id
			return redirect('wall_home')
	messages.error(request, 'login_failed', extra_tags='login')
	return redirect('wall_index')

def register(request, methods=['POST']):
	errors = User.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('wall_index')
	else:
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		request.session['user_id'] = user.id
	return redirect('wall_home')

def home(request):
	if not 'user_id' in request.session:
		return redirect('wall_index')
	context = {}
	user = User.objects.get(id=request.session['user_id'])
	context['username'] = f'{user.first_name} {user.last_name}'
	context['posts'] = Post.objects.all().order_by('-created_at')
	context['comments'] = Comment.objects.all().order_by('created_at')
	return render(request, 'home.html', context)

def logout(request, methods=['POST']):
	request.session.clear()
	return redirect('wall_index')

def post(request, methods=['POST']):
	errors = Post.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags='post')
	else:
		author = User.objects.get(id=request.session['user_id'])
		post = Post.objects.create(content=request.POST['post'], author=author)
	return redirect('wall_home')

def comment(request, methods=['POST']):
	errors = Comment.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags='comment')
	else:
		author = User.objects.get(id=request.session['user_id'])
		commented_on = Post.objects.get(id=request.POST['post_id'])
		comment = Comment.objects.create(content=request.POST['comment'], author=author, commented_on=commented_on)
	return redirect('wall_home')