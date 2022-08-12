from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User



@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    users = User.get_all()
    return render_template("users.html", all_users = users)


# whenever we create something, we need to display that html page, so we need a route for that. And we need a post route to process/load.

# create user - display route
@app.route('/users/new')
def new():
    return render_template("create_user.html")


# create user - post route
@app.route('/user/create', methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect('/users')





# edit user - display route
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        "id": id
    }
    return render_template('edit_user.html', user=User.get_one(data))



# edit user - post route
@app.route('/users/<int:id>/update', methods=["POST"])
def update_user(id):
    User.update(request.form)
    return redirect('/users')



#
@app.route('/user/<int:id>/destroy')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')



# #show individual user
@app.route('/users/<int:id>/show')
def show_user(id):
    data = {
        "id":id
    }
    return render_template('show_user.html', user=User.get_one(data))

