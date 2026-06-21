from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import db
app = FastAPI()
class SoldierIn(BaseModel):
    name: str
    rank: str | None = None
    unit: str | None = None

@app.get("/soldiers")
def list_soldiers():
    return {"soldiers": db.get_all()}
@app.get("/soldiers/{soldier_id}")
def get_soldier(soldier_id: int):
    soldier = db.get_by_id(soldier_id)
    if soldier is None:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier
@app.post("/soldiers", status_code=201)
def add_soldier(body: SoldierIn):
    new_id = db.create(body.name, body.rank, body.unit)
    return {"id": new_id, "message": "Soldier created"}
@app.put("/soldiers/{soldier_id}")
def edit_soldier(soldier_id: int, body: SoldierIn):
    data = body.model_dump(exclude_none=True)
    success = db.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}
@app.delete("/soldiers/{soldier_id}")
def remove_soldier(soldier_id: int):
    success = db.delete(soldier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted"}
