from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

##!CREATE
## TODO Show the new model form
@app.route('/recipes/new')
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
        return render_template("recipes.html",recipes = Recipe.get_all())

## TODO handle new model form
@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    else:
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'instruction': request.form['instruction'],
            'date made on': request.form['date_made_on'],
            'under_30_minutes': request.form['under_30_minutes'],
            'user_id': request.form['user_id']}
        recipe = Recipe.save(request.form) #! class method in model class, find it in ../controllers/model.py
        print(recipe)
        return redirect('/dashboard')


##! READ
@app.route('/recipes')
def recipes():
    return render_template('recipes.html', recipes = Recipe.get_all())

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template('show_model.html', recipe = Recipe.get_one(data))


# #! UPDATE
# ## TODO route to edit model form
@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template('edit_model.html', recipe = recipe)

# ## TODO handle model edit
@app.route('/edit/recipes', methods=['POST'])
def update_recipe():
    print(request.form)
    recipe = Recipe.update(request.form)
    print(recipe)
    return redirect(f"/recipes")


@app.route('/delete/<int:id>')
def destroy_recipe(id):
    data = {'id':id}
    Recipe.destroy(data)   #! class method in User class, find it in ../controllers/user.py
    return redirect('/dashboard')
