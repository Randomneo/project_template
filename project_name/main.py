from random import randint

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home() -> str:
    return f'Hello world {randint(0, 10)}'
