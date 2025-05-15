from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    ano_publicacion: int
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

class LibroOut(BaseModel):
    id: str
    titulo: str
    autor: str
    ano_publicacion: int
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

    class Config:
        from_attributes = True
