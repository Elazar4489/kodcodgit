import uvicorn
from fastapi import FastAPI
app = FastAPI()
# Query params are function arguments WITHOUT being in the path
@app.get("/users")
def get_users(role: str = "all", page: int = 1):
# Called as: GET /users?role=admin&page=2
    return {"role": role, "page": page, "users": []}
@app.get("/users/{user_id}") # user_id is required, part of the path
def get_user(user_id: int):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
