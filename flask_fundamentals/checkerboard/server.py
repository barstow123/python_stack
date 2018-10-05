from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
	world = [[0,1,0,1,0,1,0,1],
			 [1,0,1,0,1,0,1,0],
			 [0,1,0,1,0,1,0,1],
			 [1,0,1,0,1,0,1,0],
			 [0,1,0,1,0,1,0,1],
			 [1,0,1,0,1,0,1,0],
			 [0,1,0,1,0,1,0,1],
			 [1,0,1,0,1,0,1,0]]
	leny = len(world)
	lenx = len(world[0])
	return render_template('index.html', world=world, lenx=lenx, leny=leny)

@app.route('/<int:x>/<int:y>')
def dimensions(x,y):
	world = []
	colMod = 0
	for row in range(y):
		insertRow = []
		for col in range(int(x)):
			if (len(insertRow) < x):
				insertRow.append((0+colMod)%2)
			if (len(insertRow) < x):
				insertRow.append((1+colMod)%2)
		world.append(insertRow)
		colMod += 1

	leny = len(world)
	lenx = len(world[0])

	if x==0 and y==0:
		return 'error: '+1
	return render_template('index.html', world=world, lenx=x, leny=y)



app.run(debug=True)