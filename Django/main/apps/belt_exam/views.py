from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User, Job
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user_id' in request.session:
		return redirect('exam_dashboard')
	return render(request, 'exam/index.html')

def login(request):
	if 'user_id' in request.session:
		return redirect('exam_dashboard')
	user = User.objects.filter(email=request.POST['email'])
	if user:
		if bcrypt.checkpw(request.POST['password'].encode(), user[0].pw_hash.encode()):
			request.session['user_id'] = user[0].id
			return redirect('exam_dashboard')
	messages.error(request, 'login_failed', extra_tags='login')
	return redirect('exam_index')

def logout(request, methods=['POST']):
	request.session.clear()
	return redirect('exam_index')

def register(request, methods=['POST']):
	errors = User.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('exam_index')
	else:
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		request.session['user_id'] = user.id
		messages.success(request, 'user successfully added.')
	return redirect('exam_dashboard')

def dashboard(request):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	context = {}
	user = User.objects.get(id=request.session['user_id'])
	jobs = Job.objects.all()
	context['username'] = f'{user.first_name} {user.last_name}'
	context['user'] = user
	context['jobs'] = jobs
	return render(request, 'exam/dashboard.html', context)

def make_job(request):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	return render(request, 'exam/create_job.html')

def job_profile(request, id):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	context = {}
	context['job'] = Job.objects.get(id=id)
	context['user'] = User.objects.get(id=request.session['user_id'])
	return render(request, 'exam/job_profile.html', context)

def edit_job(request, id):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	context = {}
	context['job'] = Job.objects.get(id=id)
	return render(request, 'exam/edit_job.html', context)

def create_job(request, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	errors = Job.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('exam_make_job')
	else:
		categories = ''
		if 'pet-care' in request.POST:
			categories = categories + ', petcare'
		if 'garden' in request.POST:
			categories = categories + ', garden'
		if 'electrical' in request.POST:
			categories = categories + ', pet care'
		if 'category_make' in request.POST:
			addegories = request.POST['category_make']
			addegories = addegories.split(',')
			for i in range(len(addegories)):
				addegories[i] = addegories[i].strip()
				categories = '' + categories + ', ' + addegories[i]
		if len(categories) > 0:
			categories = categories[2:]
		master = User.objects.get(id=1)
		user = User.objects.get(id=request.session['user_id'])
		job = Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], category=categories, worker=master, author=user)
	return redirect('exam_dashboard')

def destroy_job(request, id, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	job = Job.objects.filter(id=id)
	if len(job) > 0:
		job.delete()
	return redirect('exam_dashboard')

def update_job(request, id, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	errors = Job.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('exam_edit_job', id=id)
	else:
		job = Job.objects.get(id=id)
		job.title = request.POST['title']
		job.description = request.POST['description']
		job.location = request.POST['location']
		job.save()
		messages.success(request, 'record successfully updated')
		return redirect('exam_dashboard')

def add_job(request, id, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	job = Job.objects.get(id=id)
	user = User.objects.get(id=request.session['user_id'])
	job.worker = user
	job.save()
	return redirect('exam_dashboard')

def drop_job(request, id, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('exam_index')
	job = Job.objects.get(id=id)
	master = User.objects.get(id=1)
	job.worker = master
	job.save()
	return redirect('exam_dashboard')