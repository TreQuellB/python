# from flask import Flask, render_template, request, redirect, session#have to connect 
# # flask,render_template, request,redirect,session which will be used in code at bottom so it can import to html

# app = Flask(__name__)
# app.secret_key = "countering"#set a secret key for security purposes

# @app.route('/')
# def index():
#     if "count" not in session:#if is not in session count will = to just 1
#         session["count"] = 1
#     else:    
#         session["count"] += 1#else if it is it will = plus 1
    
#     return render_template("index.html")#connecting to my html with render_template

# @app.route("/process", methods=["POST"])#post is a method that will post/deliver the output and change the page
# def view_count():
#     if request.form["change"]=="add":#request.form
#         session["count"] += 1#plus 1
#     elif request.form["reset_1"]=="reset":#request.form
#         session["reset_1"] = 0#if condition not met will be 0
#     return redirect("/")#redirect

# @app.route("/destroy", method="POST")#a link to destroy get rid of current url or change it
# def destroy():
#     session.clear()#to clear the session
#     return redirect("/")#redirect

# if __name__=="__main__":#a message on server when errors happen?
    
#     app.run(debug=True, port=5024)#debugging a message on server
from flask import Flask, render_template, request, redirect, session#have to connect 
app = Flask(__name__)
app.secret_key = '24'




@app.route("/")
def counter():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template("index.html")


@app.route("/add2")
def addclicks():
    if "count" in session:
        session["count"] += 1# this increase twice because the sessions are connected count is in session so thats how i get two when button press link add 2
    return redirect("/")



@app.route("/destroy")
def remove():
    if "count" in session:
        session.clear()
    return redirect("/")

if __name__=="__main__":#a message on server when errors happen?
    
    app.run(debug=True, port=5000)#debugging a message on server