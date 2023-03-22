# Adoption Application

from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()
connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SMOKEY"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
    """List all pets"""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route('/pets/add', methods=["GET", "POST"])
def add_pet():
    """Show add pet form and onsubmit post data to database"""
    # with app.test_request_context():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species =  form.species.data
        photo_url =  form.photo_url.data
        age =  form.age.data
        notes =  form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        
        # extracting data faster:
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # new_pet = Pet(**data)

        db.session.add(pet)
        db.session.commit()
        flash(f"Created new available pet, {name}, the {species}")
        return redirect('/')
    else:
        # raise
        return render_template('pet_add.html', form=form)
    

    
@app.route('/pets/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show add pet edit form and onsubmit post newly updated data to database"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url =  form.photo_url.data
        pet.notes =  form.notes.data
        pet.available =  form.available.data
        
        db.session.commit()
        flash(f"Updated info of {pet.name}, the {pet.species}")
        return redirect(f'/')
    else:
        # raise
        return render_template('pet_edit.html', form=form, pet=pet)



