from fastapi import FastAPI
from routers import libro, elemento
from typing import Union

app = FastAPI(title="API Biblioteca - MongoDB")

app.include_router(libro.router)
app.include_router(elemento.router)

@app.get('/')
def read_root():
    return {'message': 'Hello World form FastAPI and Koyeb'}