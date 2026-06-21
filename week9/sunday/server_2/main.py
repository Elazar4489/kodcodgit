from wsgiref.util import application_uri

from fastapi import FastAPI

import db

app = FastAPI()

@app.get("/schema/soldiers")
def get_schema_of_soldiers():
    return db.get_schema_of_soldiers()

@app.get("/schema/soldiers_rooms")
def get_schema_of_soldiers_rooms():
    return db.get_schema_of_soldiers_rooms()

