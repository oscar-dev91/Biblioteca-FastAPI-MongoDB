"""
🚀 **API Biblioteca - MongoDB**

Bienvenido a la API de gestión de biblioteca desarrollada con **FastAPI** y conectada a una base de datos **MongoDB**.

Este sistema permite la administración completa de los siguientes recursos:
- 📚 Libros
- 📰 Revistas
- 💿 DVDs
- 📦 Elementos generales de la biblioteca

🔌 **Rutas incluidas:**
- `/libros`: Endpoints para gestión de libros.
- `/revistas`: Endpoints para gestión de revistas.
- `/dvds`: Endpoints para gestión de DVDs.
- `/elementos`: Endpoints para listar o buscar cualquier tipo de elemento.

🛠️ **Tecnologías utilizadas**:
- FastAPI
- MongoDB
- Pydantic
- Async IO

🌐 **Ruta raíz `/`**:
- Devuelve un mensaje de bienvenida: `{ "message": "Hello World from FastAPI and Koyeb" }`

---
💡 Puedes acceder a la documentación interactiva automáticamente generada en:
- Swagger UI: `/docs`
- ReDoc: `/redoc`
"""

from fastapi import FastAPI
from routers import libro, elemento, dvd, revista
from typing import Union

app = FastAPI(title="API Biblioteca - MongoDB")

app.include_router(libro.router)
app.include_router(elemento.router)
app.include_router(dvd.router)
app.include_router(revista.router)

@app.get('/')
def read_root():
    return {'message': 'Hello World form FastAPI and Koyeb'}