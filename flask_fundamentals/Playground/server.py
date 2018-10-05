from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
	return render_template('index.html')

@app.route('/play/<int:x>')
def playx(x):
	return render_template('xtimes.html', times=x)

@app.route('/play/<int:x>/<color>')
def play_x_color(x, color):
	return render_template('x_times_color.html', times=x, color=color)

app.run(debug=True)