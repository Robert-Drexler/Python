from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.painting import Painting

##!CREATE
## TODO Show the new model form
@app.route('/paintings/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('new_model.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template("paintings.html",paintings = Painting.get_all())

## TODO handle new model form
@app.route('/create/painting', methods=['POST'])
def create_painting():
    print(request.form)
    if not Painting.validate_painting(request.form):
        return redirect('/paintings/new')
    else:
        data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'price': request.form['price'],
            'user_id': request.form['user_id']}
        painting = Painting.save(request.form) #! class method in model class, find it in ../controllers/model.py
        print(painting)
        return redirect('/paintings')


##! READ
@app.route('/paintings')
def paintings():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('paintings.html', paintings = Painting.get_all())

@app.route('/paintings/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template('show_model.html', painting = Painting.get_one(data))


# #! UPDATE
# ## TODO route to edit model form
@app.route('/paintings/<int:id>/edit')
def edit_painting(id):
    data = {'id': id}
    painting = Painting.get_one(data)
    return render_template('edit_model.html', painting = painting)

# ## TODO handle model edit
@app.route('/edit/paintings', methods=['POST'])
def update_painting():
    print(request.form)
    painting = Painting.update(request.form)
    print(painting)
    return redirect(f"/paintings")


@app.route('/delete/<int:id>')
def destroy_painting(id):
    data = {'id':id}
    Painting.destroy(data)   #! class method in User class, find it in ../controllers/user.py
    return redirect('/paintings')

