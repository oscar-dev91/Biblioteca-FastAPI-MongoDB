from pydantic import BaseModel

class LibroCreate(BaseModel):
    """
Esquema de entrada para la creación de un nuevo libro.

Define los campos necesarios para registrar un libro en el sistema.

Atributos:
- titulo (str): Título del libro.
- autor (str): Nombre del autor del libro.
- ano_publicacion (int): Año en que se publicó el libro.
- isbn (str): Código ISBN del libro.
- numero_paginas (int): Total de páginas del libro.
- genero (str): Género literario del libro.
- editorial (str): Nombre de la editorial.
    """
    titulo: str
    autor: str
    ano_publicacion: int
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

class LibroOut(BaseModel):
    """
Esquema de salida que representa la información de un libro registrada en el sistema.

Incluye todos los campos del libro junto con su identificador único.

Atributos:
- id (str): Identificador único del libro.
- titulo (str): Título del libro.
- autor (str): Nombre del autor.
- ano_publicacion (int): Año de publicación.
- isbn (str): Código ISBN.
- numero_paginas (int): Total de páginas.
- genero (str): Género literario.
- editorial (str): Editorial del libro.
    """
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
