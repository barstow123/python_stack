from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	return render(request, 'index.html')

def generate(request, methods=['POST']):
	return redirect('/random_number_generater')
