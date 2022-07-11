from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/8/8')          # The "@" decorator associates this route with the function immediately following#always have forward/ in front
def hello_world1():
    return render_template('index8_8.html')  # Return the string 'Hello World!' as a response

@app.route('/8/4')          # The "@" decorator associates this route with the function immediately following#always have forward/ in front
def hello_world2():
    return render_template('index8_4.html')  # Return the string 'Hello World!' as a response

@app.route('/10/10')          # The "@" decorator associates this route with the function immediately following#always have forward/ in front
def hello_world3():
    return render_template('index10_10.html')  # Return the string 'Hello World!' as a response


# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world3():
#     return render_template('index.html')  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

