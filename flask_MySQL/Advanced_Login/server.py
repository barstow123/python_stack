from flask import Flask, render_template, session, request, redirect, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import math

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-z]')


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "dirty sex joke!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def create():

    passStrength = 0
    hidden = {
        'password' : request.form['password'],
        'password_confirm' : request.form['password_confirm']
    }
    if hidden['password']:
        pw_hash = bcrypt.generate_password_hash(hidden['password'])
    else:
        flash('Password must not be left blank!', 'password')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(hidden['password'])
    data = {
        'password' : pw_hash,
        'email': request.form['email'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    mysql = connectToMySQL('simpleWall')
    email_verify = mysql.query_db("SELECT email FROM user WHERE email = %(email)s;", data)
    password = request.form['password']

    if len(email_verify) > 0:
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
        flash("Name must be 2+ characters", 'last_name')
    if hidden['password'] != hidden['password_confirm']:
        flash('Passwords do not match!', 'password')
    passFlash = []

    if (len(password) >= 8):                                   #tests if password is at least of length 8
        passStrength += 1
    else:
        passFlash.append(['Password should be at least 8 characters long!', 'password'])
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

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        mysql = connectToMySQL('simpleWall')
        query = "INSERT INTO user (first_name,last_name,email,password_hash, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        new_user_id = mysql.query_db(query, data)
        session['user_id'] = new_user_id
        session['first_name'] = data['first_name']
        return redirect('/home')


@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("simpleWall")
    query = "SELECT * FROM user WHERE email = %(email)s;"

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
            session['user_id'] = results[0]['id']
            session['first_name'] = results[0]['first_name']
            return redirect('/home')
    flash("You could not be logged in",'login')
    return redirect("/")

@app.route('/home')
def home():
    mysql = connectToMySQL("simpleWall")
    query = "SELECT first_name, id FROM user WHERE id != "+str(session['user_id'])+";"
    message_query = "SELECT * FROM message JOIN user ON message.author_id = user.id WHERE recipient_id = "+str(session['user_id'])+" AND content != '' ORDER BY message.created_at DESC;"
    site_users = mysql.query_db(query)

    mysql = connectToMySQL("simpleWall")
    user_messages = mysql.query_db(message_query)

    for i in range(len(user_messages)):
        user_messages[i]['sent_ago'] = datetime.now() - user_messages[i]['created_at']
        user_messages[i]['sent_ago'] = user_messages[i]['sent_ago'].seconds
        num_seconds = user_messages[i]['sent_ago']
        if num_seconds >= 60*60*24:
            user_messages[i]['sent_ago'] = str(int(user_messages[i]['sent_ago']/(60*60*24))) + " days"
        elif num_seconds >= 60*60:
            user_messages[i]['sent_ago'] = str(int(user_messages[i]['sent_ago']/(60*60))) + " hours"
        elif num_seconds >= 60:
            user_messages[i]['sent_ago'] = str(int(user_messages[i]['sent_ago']/60)) + " minutes"
        else:
            user_messages[i]['sent_ago'] = str(int(user_messages[i]['sent_ago'])) + " seconds"
    if user_messages == False:
        user_message = [{}]
    num_messages = len(user_messages)
    mysql = connectToMySQL("simpleWall")
    num_sent_messages = mysql.query_db("SELECT COUNT(content) from message WHERE author_id = "+str(session['user_id'])+";")
    return render_template('home.html', site_users=site_users, messages = user_messages, num_messages=num_messages, num_sent_messages=num_sent_messages)

@app.route('/send', methods=['POST'])
def sendMessage():
    if len(request.form['message']) < 1:
        flash('message cannot be blank!', 'message')
        return redirect('/home')
    mysql = connectToMySQL("simpleWall")
    query = "INSERT INTO message (author_id, recipient_id, content, created_at, updated_at) VALUES (%(author_id)s, %(recipient_id)s, %(content)s, NOW(), NOW());"
    data = {
        'author_id': session['user_id'],
        'recipient_id': request.form['recipient_id'],
        'content': request.form['message']
    }
    new_message_id = mysql.query_db(query, data)
    return redirect('/home')

@app.route('/delete', methods=['POST'])
def delete():
    mysql = connectToMySQL("simpleWall")
    query = "UPDATE message SET content = '' WHERE id = %(delete_id)s;"
    data = {
        'delete_id': request.form['delete_id']
    }
    mysql.query_db(query, data)
    return redirect('/home')

if __name__=="__main__":
    app.run(debug=True)