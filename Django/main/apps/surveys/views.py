from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'index.html')

def submit(request):
	if request.method == 'POST':

		if 'times' in request.session:
			request.session['times'] += 1
		else:
			request.session['times'] = 0

		request.session['first_name'] = request.POST['first_name']
		request.session['location'] = request.POST['location']
		request.session['fav_language'] = request.POST['fav_language']
		request.session['comment'] = request.POST['comment']
		print('session: '+ str(request.session))

		return redirect('/surveys/success')

	return redirect('/surveys')

def success(request):
	context = {
		'first_name': request.session['first_name'],
		'location': request.session['location'],
		'fav_language': request.session['location'],
		'comment': request.session['comment']
	}
	return render(request, 'success.html', context)