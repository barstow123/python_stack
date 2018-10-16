from django.shortcuts import render, redirect
import re
from datetime import datetime

# Create your views here.
def index(request):
	if 'words' in request.session:
		data = {'data':request.session['words']}
	else:
		data = {'data':[]}

	print('data: ', str(data))
	return render(request, 'index.html', data)

def add_to_session(request, methods=['POST']):

	print(request.POST)

	word = request.POST['word'].split(' ')[0]
	if 'big_text' in request.POST:
		showbig = 1.7
	else:
		showbig = 1

	if 'color' not in request.POST:
		color = 'black'
	else: 
		color = request.POST['color']

	data = {
		'word': word,
		'color': color,
		'big_text': showbig,
		'created_at': datetime.now().strftime('%I:%M %p, %B %d %Y')
	}
	print('data.created_at :' + data['created_at'])
	if 'words' in request.session:
		current_session_words_data = request.session['words']
	else:
		current_session_words_data = []
	current_session_words_data.append(data)
	request.session['words'] = current_session_words_data
	return redirect('/session_words')

def clear_session(request, methods=['POST']):
	request.session.clear()
	return redirect('/session_words/')