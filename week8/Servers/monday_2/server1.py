import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/greet")
def get_hello(name="world"):
    return {"message": f"Hello, {name}!"}
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)

