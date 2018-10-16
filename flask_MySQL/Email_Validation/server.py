from flask import Flask, session, render_template, redirect, request, flash
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'dirty sex joke'

@app.route('/')
def index():
    mysql = connectToMySQL("email_validation")
    all_emails = mysql.query_db("SELECT * FROM email")
    print("Fetched all emails", all_emails)
    return render_template('index.html', emails = all_emails)

@app.route('/register_email', methods=['POST'])
def create():
    mysql = connectToMySQL("email_validation")
    query = "INSERT INTO email (email, created_at) VALUES (%(email)s, NOW());"
    email_RE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    data = {
            'email': request.form['email'],
           }
    if not email_RE.match(data['email']):
        print('invalid email')
        flash('please enter a valid email')
    else:
        print('valid email')
        new_email_id = mysql.query_db(query, data)
    return redirect('/')

if (__name__) == ('__main__'):
	app.run(debug=True)