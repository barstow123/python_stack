from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'Secretness'


@app.route('/')
def default():
	if 'guess' in session:
		guess = int(session['guess'])
	else:
		guess = 101

	if not 'answer' in session:
		session['answer'] = int(random.random()*99 +1)
	return render_template('index.html', guess=guess, answer=int(session['answer']))

@app.route('/submit', methods=["POST"])
def guess():
	session['guess'] = request.form['guess']
	print('guess + ' + str(session['guess']) + '\nanswer: ' + str(session['answer']))
	return redirect('/')


if __name__==('__main__'):
	app.run(debug=True)