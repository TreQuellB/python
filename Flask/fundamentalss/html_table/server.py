from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following#always have forward/ in front
def users():
    users = [
{'first_name' : 'Michael', 'last_name' : 'Choi'},
{'first_name' : 'John', 'last_name' : 'Supsupin'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]


    return render_template('index.html', users=users)  # Return the string 'Hello World!' as a response




# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world3():
#     return render_template('index.html')  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

