from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	context = {
		"email" : "blog@gmail.com",
		"name" : "mike"
	}
	return render(request, "ourApp/index.html", context)

def new(request):
	response = "Hello, I am routed to /new"
	return HttpResponse(response)

def create(request):
	response = "you have been routed to /create"
	return HttpResponse(response)

def number(request, num):
	response = "is your number %s" % num
	return HttpResponse(response)

def editBlogNum(request, num):
	response = "placeholder for edit blog # %s" % num
	return HttpResponse(response)

def destroy(request, num):
	return redirect('/')