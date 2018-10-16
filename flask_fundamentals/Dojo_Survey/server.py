from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
import re
app.secret_key = 'more inappropriate sex jokes'

@app.route('/')
def default():
	return render_template('index.html')

@app.route('/submitted')
def submitted():
	email = session['data'][0]
	comment = session['data'][1]
	session.pop('data')
	return render_template("submitted.html", email=email, comment=comment)


@app.route('/result', methods=['POST'])
def create_user():
	emailRE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	email = request.form['email']
	password = request.form['password']
	comment = request.form['comment']
	passStrength = 0

	if (len(password) < 1):
		flash('password cannot be blank!')
	elif(len(password) > 8):								#tests if password is at least of length 8
		passStrength += 1
	if (re.compile(r'.*[A-Z].*[A-Z]').match(password)):		#tests for at least 2 capital letters
		passStrength += 1
	if (re.compile(r'.*[!@#$&*]').match(password)):			#tests for at least one special character
		passStrength += 1
	if (re.compile(r'.*[0-9].*[0-9]').match(password)):		#tests for at least 2 digits
		passStrength += 1
	if (re.compile(r'.*[a-z].*[a-z].*[a-z]').match(password)):	#tests for at least 3 lower case letters
		passStrength += 1


	if len(email) < 1:
		flash("Email cannot be blank!")
	elif not emailRE.match(email):
		flash("Invalid Email Address!")
	if len(comment) < 1:
		flash("You had better leave us a comment, scrub!")
	elif len(comment) > 120:
		flash('Your comment is too long')
	if passStrength < 3:
		flash('you will need a stronger password')

	session['data'] = [email, comment]

	if '_flashes' in session.keys():
		return redirect("/")
	else:
		return redirect("/submitted")

app.run(debug=True)