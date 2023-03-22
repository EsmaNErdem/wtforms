"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="cat", photo_url="https://d.newsweek.com/en/full/1920025/cat-its-mouth-open.jpg?w=1600&h=1600&q=88&f=b7a44663e082b8041129616b6b73328d", available=True)
bowser = Pet(name='Bowser', species="dog", photo_url="https://cdn.shopify.com/s/files/1/2609/7926/articles/AdobeStock_274099078.jpg?v=1620400547", available=True)
spike = Pet(name='Spike', species="porcupine", photo_url="https://i.pinimg.com/736x/ea/e2/72/eae272d076fc70723258782c8a217fde.jpg", available=True)
smokey = Pet(name='Smokey', species="cat", photo_url="https://www.zooplus.co.uk/magazine/wp-content/uploads/2019/03/maine-coon-cat-breed.jpg", available=False)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)
db.session.add(smokey)

# Commit--otherwise, this never gets saved!
db.session.commit()