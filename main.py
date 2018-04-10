from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    if input = True:
        username = request.form("username")
        return render_template("welcome.html", username = username)
    else:
        return render_template("edit.html")




app.run()