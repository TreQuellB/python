from flask_app import app
from flask import render_templates
@app.route("/")
def display_login():
    return render_templates('login.html')

@app.route('/user/registration')