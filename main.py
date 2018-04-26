from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/", methods = ["POST", "GET"])
def index():
    
    
        
    return render_template('edit.html')
    
@app.route("/welcome", methods = ["POST", "GET"])
def welcome():

    
    username =  request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify = request.form['verify']

    username_error = ''
    email_error = ''
    password_error = ''
    verify_error = ''
    
    if username == "" or password =="" or verify =="":

        return 'please fill in all areas'
    
    elif  " " in username or " " in password:

        return username_error == 'please do not use blank spaces'
    
    elif len(username) < 3 or len(username) > 20:

        return username_error == 'invalid name length please reenter'
    
    elif len(password) < 3 or len(password) > 20:

        return password_error == 'invalid password length please reenter'
    
    elif password == verify:
    
        return render_template('/welcome.html', username=username)
    
    else:
        
        return verify_error == 'please make sure your passwords match!'
    
   
    if "@" + " " in email or " " + "@" in email:
        return email_error == 'please reenter a valid email address'

    elif "@" not in email:

        return email_error == 'please reenter a valid email address'



app.run()