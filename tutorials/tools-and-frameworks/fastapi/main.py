from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
