from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User, Book, Author, Review
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user_id' in request.session:
		return redirect('belt_home')
	return render(request, 'belt/log_in.html')

def login(request):
	user = User.objects.filter(email=request.POST['email'])
	if user:
		if bcrypt.checkpw(request.POST['password'].encode(), user[0].pw_hash.encode()):
			request.session['user_id'] = user[0].id
			return redirect('belt_home')
	messages.error(request, 'login_failed', extra_tags='login')
	return redirect('belt_index')

def register(request, methods=['POST']):
	errors = User.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('belt_index')
	else:
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		request.session['user_id'] = user.id
	return redirect('belt_home')

def home(request):
	if not 'user_id' in request.session:
		return redirect('belt_index')
	context = {}
	user = User.objects.get(id=request.session['user_id'])
	books = Book.objects.all()
	context['user'] = user
	context['username'] = f'{user.first_name} {user.last_name}'
	context['reviews'] = Review.objects.all().order_by('-created_at')[:5]
	context['books'] = books
	return render(request, 'belt/home.html', context)

def logout(request, methods=['POST']):
	request.session.clear()
	return redirect('belt_index')

def review(request):
	if not 'user_id' in request.session:
		return redirect('belt_index')
	context = {}
	authors = Author.objects.all().order_by('-name')
	context['authors'] = authors
	return render(request, 'belt/add_review.html', context)

def post_review(request, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('belt_index')
	errors = Review.objects.validator(request.POST)
	if len(errors):
		print(f'found errors: {errors}')
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect('belt_review')
	else:
		if len(request.POST['make_author']) > 0:
			author_name = request.POST['make_author']
		else:
			author_name = request.POST['choose_author']

		if Author.objects.filter(name=author_name):
			author = Author.objects.get(name=author_name)
		else:
			author = Author.objects.create(name=author_name)
		book = Book.objects.filter(author=author)
		if book:
			book = book[0]
		if not book:
			book = Book.objects.create(title=request.POST['title'], author=author)
		review_author = User.objects.get(id=request.session['user_id'])
		review = Review.objects.create(content=request.POST['content'], rating=request.POST['rating'], review_author=review_author, book_reviewed=book)
	return redirect('belt_home')

def profile(request, id):
	context = {}
	profile_user = User.objects.get(id=id)
	context['logged_in'] = False
	if 'user_id' in request.session:
		user = User.objects.get(id=request.session['user_id'])
		context['user'] = user
		context['logged_in'] = True
	context['profile_user'] = profile_user
	context['prof_user_num_reviews'] = User.objects.get(id=id).reviews.count()
	context['profile_user_reviews'] = User.objects.get(id=id).reviews.all()
	return render(request, 'belt/profile.html', context)

def book(request, book_id):
	context = {}
	book = Book.objects.get(id=book_id)
	context['logged_in'] = False
	if 'user_id' in request.session:
		user = User.objects.get(id=request.session['user_id'])
		context['user'] = user
		context['logged_in'] = True
	context['book'] = book
	context['book_reviews'] = Book.objects.get(id=book_id).reviews.all()
	return render(request, 'belt/book.html', context)

def destroy(request, review_id, methods=['POST']):
	if not 'user_id' in request.session:
		return redirect('belt_index')
	r = Review.objects.get(id=review_id)
	b = r.book_reviewed
	r.delete()
	if len(b.reviews.all()) < 1:
		b.delete()


	return redirect(request.POST['return_index'])