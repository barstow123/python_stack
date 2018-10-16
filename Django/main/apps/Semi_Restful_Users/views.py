from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
	print('in index!')
	context = {}
	context['users'] = User.objects.all()
	print('context: ' +str(context))
	return render(request, 'index.html', context)

def show(request, id):
	print('got to show!')
	context = {}
	context['user'] = User.objects.get(id=id)
	return render(request, 'show.html', context)

def delete(request, id):
	u = User.objects.get(id=id)
	u.delete()
	return redirect('index')

def edit(request, id):
	context = {}
	context['user'] = User.objects.get(id=id)
	return render (request, 'edit.html', context)

def add_user(request):
	return render(request, 'add_user.html')

def create_user(request, methods=['POST']):
	print('creating user')
	User.objects.create(name=request.POST['name'], email=request.POST['email'])
	return redirect('index')

def update_user(request, id, methods=['POST']):
	print('updating user')
	u = User.objects.get(id=id)
	u.name = request.POST['name']
	u.email = request.POST['email']
	u.save()
	return redirect('index')
