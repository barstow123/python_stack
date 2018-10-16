from flask import Flask, render_template, session, request, redirect, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-z]')


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def create():

    mysql = connectToMySQL('somethingnew')
    email_verify = mysql.query_db("SELECT email FROM user;")
    passStrength = 0
    query = "INSERT INTO user (first_name,last_name,email,password_hash) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
    hidden = {
        'password' : request.form['password'],
        'password_confirm' : request.form['password_confirm']
    }
    pw_hash = bcrypt.generate_password_hash(hidden['password'])
    data = {
        'password' : pw_hash,
        'email': request.form['email'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    password = request.form['password']

    for email in email_verify:
        print("ZOWIEWOWIE")
        if email['email'] == data['email']:
            print("WOWIEZOWIE")
            flash("Email already exists!", 'email')
    if len(data['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(data['email']):
        flash("Invalid Email Address!", 'email')

    if len(data['first_name']) < 1:
        flash("Name cannot be blank!", 'first_name')
    elif len(data['first_name']) <= 2:
        flash("Name must be 2+ characters", 'first_name')

    if len(data['last_name']) < 1:
        flash("Name cannot be blank!", 'last_name')
    elif len(data['last_name']) <= 2:
        flash('Name must be 2+ characters', 'last_name')
    if hidden['password'] != hidden['password_confirm']:
        flash('Passwords do not match!', 'password')

    passFlashes = []
    if (len(password) >= 8):                                   #tests if password is at least of length 8
        passStrength += 1
    else:
        passFlashes.append(['Password should be at least 8 characters long!', 'password'])

    if (re.compile(r'.*[A-Z].*[A-Z]').match(password)):        #tests for at least 2 capital letters
        passStrength += 1
    else:
        passFlash.append(["Password should contain one capital letter", 'password'])

    if (re.compile(r'.*[!@#$&*]').match(password)):            #tests for at least one special character
        passStrength += 1
    else:
        passFlash.append(["Password should contain one special character", 'password'])

    if (re.compile(r'.*[0-9].*[0-9]').match(hidden['password'])):        #tests for at least 2 digits
        passStrength += 1
    else:
        passFlash.append(["Password should contain at least two digits", 'password'])

    if (re.compile(r'.*[a-z].*[a-z].*[a-z]').match(hidden['password'])):    #tests for at least 3 lower case letters
        passStrength += 1
    else:
        passFlash.append(["Password should contatin at least 3 lower case letters", 'password'])

    if passStrength < 3:
        for flashed in passFlash:
            flash(flashed[0], flashed[1])


    if '_flashes' in session.keys() or passStrength <4:
        return redirect("/")
    else:
        mysql = connectToMySQL('somethingnew')
        new_user_id = mysql.query_db(query, data)
        return redirect('/success')


@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("somethingnew")
    query = "SELECT email,password_hash FROM user WHERE email = %(email)s;"

    hidden = {
        'password' : request.form['password']
    }

    pw_hash = bcrypt.generate_password_hash(hidden['password'])

    data = {
        'password' : pw_hash,
        'email': request.form['email'],
    }

    results = mysql.query_db(query, data)
    if results:
        if bcrypt.check_password_hash(results[0]['password_hash'], hidden['password']):
                    return redirect('/success')
    flash("You could not be logged in",'login')
    return redirect("/")

@app.route('/success')
def success():
    if ('user_id' not in session.keys()):
        return redirect('/')
    return render_template('success.html')
if __name__=="__main__":
    app.run(debug=True)
