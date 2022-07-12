from flask import Flask, session,render_template,redirect,request
app=Flask(__name__)
app.secret_key="24"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/processed",methods=["POST"])#methods is plural in the app route
def processing():
    session["name"]=request.form["name"]#acessing the html throught the session and request to get the key and values
    session["location"]=request.form["location"]#acessing the html throught the session and request to get the key and values
    session["language"]=request.form["language"]#acessing the html throught the session and request to get the key and values
    session["comments"]=request.form["comments"]#acessing the html throught the session and request to get the key and values
    
    return redirect("/results")#redirect is looking for the route

@app.route("/results")#route must match redirect
def result_1():
    
    return render_template("index_1.html")


if __name__ == "__main__":
    app.run(debug=True)