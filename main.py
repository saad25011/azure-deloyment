from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚀 FastAPI app is working!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello, {name}!"}
