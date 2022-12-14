"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb cards")
os.system("createdb cards")

model.connect_to_db(server.app)
model.db.create_all()

for n in range(10):
    email = f'user{n}@test.com' 
    password = 'test'

    db_user = crud.create_user(email, password)
    model.db.session.add(db_user)


model.db.session.commit()