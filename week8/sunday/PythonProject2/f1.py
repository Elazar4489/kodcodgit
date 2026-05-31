from fastapi import FastAPI

app = FastAPI()
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}

if __name__ == "__name__":
