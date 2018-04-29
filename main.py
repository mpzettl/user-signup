from flask import Flask, request, redirect, render_template
import cgi

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

    fill_error = 'please fill in all areas'
    username_error = 'please do not use blank spaces'
    userlen_error = 'please enter a username between 3 and 20 characters'
    email_error = 'please reenter a valid email address'
    password_error = 'invalid password length please reenter'
    verify_error = 'please make sure your passwords match!'
    
    if username == "" or password =="" or verify =="":

        return render_template('edit.html', fill_error=fill_error)
    
    elif  " " in username or " " in password:

        return  render_template('edit.html', username_error=username_error)
    
    elif len(username) < 3 or len(username) > 20:

        return render_template('edit.html', userlen_error=userlen_error)
    
    elif len(password) < 3 or len(password) > 20:

        return render_template('edit.html', password_error=password_error)
    
    elif "@" not in email:

        return render_template('edit.html', email_error=email_error)
        
    elif password == verify:
    
        return render_template('welcome.html', username=username)
    
    else:
        
        return render_template('edit.html', verify_error=verify_error)  

    



app.run()