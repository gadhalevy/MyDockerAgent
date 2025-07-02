from fastapi import FastAPI
import os

API_KEY=os.getenv("APIKEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

app = FastAPI()

@app.get("/")
def read_index():
    return {"message": "Welcome to the FastAPI application בני זונות!"}