from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/dojo')
def dojo():
	return 'Dojo'

@app.route('/say/<name>')
def say_hi(name):
	print(name)
	return 'Hi, '+name

@app.route('/repeat/<num>/<word>')
def repeate(num, word):
	num = int(num)
	print(word*num)
	return word*num

app.run(debug=True)