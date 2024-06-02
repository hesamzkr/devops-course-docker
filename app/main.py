from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Interpreted Jenkins + Docker Test"}
