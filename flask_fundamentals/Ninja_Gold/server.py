from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'inappropriate sex joke'


@app.route('/')
def default():
	if 'gold' in session:
		gold = session['gold']
	else:
		session['gold'] = 0
	if 'activities' in session:
		activites = session['activities']
	else:
		session['activities'] = []
	return render_template('index.html', data)

@app.route('/updateGold', methods=['POST'])
def updateGold():
	if request.form['action'] == 'farm':
		farmedGold = random.randrange(10,21)
		session['gold'] += farmedGold
		session['activities'].append(['earned ' + str(farmedGold) + ' gold from farming', 0])

	if request.form['action'] == 'cave':
		session['gold'] += 15
		session['activities'].append(['earned 15 gold from exploring the cave', 0])

	if request.form['action'] == 'house':
		foundHouseGold = random.randrange(2,6)
		session['gold'] += foundHouseGold
		session['activities'].append(['earned ' + str(foundHouseGold) + ' gold from a house', 0])

	if request.form['action'] == 'casino':
		casinoExpense = random.randrange(-50,51)
		session['gold'] += casinoExpense
		if(casinoExpense >= 0):
			session['activities'].append(['won ' + str(casinoExpense) + ' gold from the casino!', 0])
		else:
			session['activities'].append(['lost ' + str(casinoExpense) + ' gold from the casino...ouch', 1])
	return redirect('/')



if __name__==('__main__'):
	app.run(debug=True)