
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/numbers/{n}")
def get_numbers(n: int):
    return {"numbers": list(range(1, n+1))}

@app.get("/greet")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}
