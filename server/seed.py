#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Owner, Pet

db.init_app(app)

fake = Faker()

with app.app_context():
    Pet.query.delete()
    Owneer.query.delete()

    owners = []
    for n in range(50):
        owner = Owner(name=fake.name())
        owners.append(owner)

    db.session.add_all(owners)

    pets = []
    for n in range(50):
        pet = Pet(name=fake.name())
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()