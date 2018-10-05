from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def default():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
	email = request.form['email']
	checked = request.form['checked']
	return render_template('submitted.html', email=email, checked=checked)

app.run(debug=True)