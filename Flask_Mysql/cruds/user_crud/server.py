from flask_app import app#targetting the app.run
from flask_app.controllers import users

if __name__=="__main__":# Ensure this file is being run directly and not from a different module    
    app.run(debug=True)# Run the app in debug mode.