from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import queries
import db
import reports
import uvicorn

#===========================================================================================================
#===========================================================================================================
app = FastAPI()

class SoldierIn(BaseModel):
    name: str
    rank: str | None = None
    unit: str | None = None

#===========================================================================================================

@app.get("/soldiers")
def list_soldiers(
    rank: str | None = Query(default=None),
    unit: str | None = Query(default=None),
    sort: str = Query(default="asc")
    ):
    if rank:
        return {"soldiers": queries.get_by_rank(rank)}
    elif unit:
        return {"soldiers": queries.get_by_unit(unit)}
    elif sort:
        return {"soldiers": queries.get_active_sorted(sort)}
    else:
        return db.show_all()

#===========================================================================================================

@app.get("/soldiers/units")
def get_distinct_units():
    return queries.get_distinct_units()

#===========================================================================================================

@app.get("/soldiers/search/{term}")
def search_by_name(term: str):
    search = queries.search_by_name(term)
    if search is None:
        raise HTTPException(status_code = 404, detail = "invalid data, you must enter '%'")
    return search

#===========================================================================================================

@app.get("/soldiers/missing-rank")
def get_missing_rank():
    return queries.get_missing_rank()

#===========================================================================================================

@app.get("/soldiers/stats/summary")
def get_summary():
    return reports.get_summary()

#===========================================================================================================

@app.get("/stats/units")
def count_by_unit():
    return {"units": reports.count_by_unit()}

#===========================================================================================================

@app.get("/soldiers/stats/understaffed")
def get_units_with_multiple_soldiers():
    return reports.get_units_with_multiple_soldiers()

#===========================================================================================================

@app.get("/soldiers/formatted")
def get_formatted_soldiers():
    res= reports.get_formatted_soldiers()
    print(res)
    return {"formatted soldiers":res }

#===========================================================================================================

@app.get("/soldiers/missing-rank")
def get_missing_data():
    return {"missing_data": reports.get_missing_data()}

#===========================================================================================================

@app.get("/soldiers/{id}")
def show_one(ind: int):
    soldier = db.show_one(ind)
    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier

#===========================================================================================================

@app.post("/soldiers")
def create(body: SoldierIn):
    new_id = db.create(body.name, body.rank, body.unit)
    return {"id": new_id, "message": "Soldier created"}

#===========================================================================================================

@app.put("/soldiers/{id}")
def update(ind: int, body: SoldierIn):
    data = body.model_dump(exclude_none = True)
    success = db.update(ind, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}

#===========================================================================================================

@app.delete("/soldiers/{id}")
def delete(ind):
    success = db.delete(ind)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted"}

#===========================================================================================================
#===========================================================================================================

if __name__ == "__main__":
    uvicorn.run(app, host= "localhost", port=8000)















