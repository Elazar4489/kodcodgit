from wsgiref.util import application_uri

from fastapi import FastAPI

import db

app = FastAPI()

@app.get("/schema")
def det_schema():
    return db.get_schema()