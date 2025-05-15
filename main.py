from fastapi import FastAPI
from routers import libro, elemento

app = FastAPI(title="API Biblioteca - MongoDB")

app.include_router(libro.router)
app.include_router(elemento.router)
