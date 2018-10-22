from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
	context = {}
	context['courses'] = Course.objects.all()
	return render (request, 'index.html', context)

def destroy(request, id):
	print('in the destroy route')
	if request.method == 'POST':
		c = Course.objects.get(id=id)
		c.delete()
		return redirect('course_index')
	else:
		context = {}
		context['course'] = Course.objects.get(id=id)
		return render(request, 'destroy.html', context)

def create(request, methods=['POST']):
	print('in the create route')
	errors = Course.objects.validator(request.POST)
	if len(errors):
		print('found errors')
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('course_index')
	else:
		Course.objects.create(name=request.POST['name'], description=request.POST['desc'])
	return redirect('course_index')