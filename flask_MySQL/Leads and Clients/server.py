from flask import Flask, session, render_template, redirect, request
from mysqlconnection import connectToMySQL
import json
app = Flask(__name__)
app.secret_key = 'dirty sex joke'

@app.route('/')
def index():
    mysql = connectToMySQL("customerleads")
    customers = mysql.query_db("SELECT * FROM customer")
    print("Fetched all customers", customers)
    return render_template('index.html', customers = customers)

if __name__ == ('__main__'):
	app.run(debug=True)