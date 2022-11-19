from random import randint

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return f'Hello world {randint()}'
