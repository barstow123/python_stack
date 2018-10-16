from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
	if 'gold' in request.session:
		gold = request.session['gold']
	else:
		request.session['gold'] = 0
	if 'activities' in request.session:
		activites = request.session['activities']
	else:
		request.session['activities'] = []

	return render(request, 'ninja_gold/index.html')

def proccess_gold(request, methods=['POST']):

	activities = request.session['activities']

	if request.POST['action'] == 'farm':
		farmedGold = random.randrange(10,21)
		request.session['gold'] += farmedGold
		activities.append({'message': 'earned ' + str(farmedGold) + ' gold from farming', 'status': 0})
		request.session['activities'] = activities

	if request.POST['action'] == 'cave':
		request.session['gold'] += 15
		activities.append({'message':'earned 15 gold from exploring the cave', 'status': 0})
		request.session['activities'] = activities

	if request.POST['action'] == 'house':
		foundHouseGold = random.randrange(2,6)
		request.session['gold'] += foundHouseGold
		activities.append({'message': 'earned ' + str(foundHouseGold) + ' gold from a house', 'status': 0})
		request.session['activities'] = activities

	if request.POST['action'] == 'casino':
		casinoExpense = random.randrange(-50,51)
		request.session['gold'] += casinoExpense
		if(casinoExpense >= 0):
			activities.append({'message': 'won ' + str(casinoExpense) + ' gold from the casino!', 'status': 0})
			request.session['activities'] = activities
		else:
			activities.append({'message': 'lost ' + str(casinoExpense) + ' gold from the casino...ouch', 'status': 1})
			request.session['activities'] = activities
	return redirect('/ninja_gold/')