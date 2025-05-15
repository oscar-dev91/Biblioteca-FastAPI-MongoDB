from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class Libro(Model):
    """
Modelo que representa un libro en la biblioteca.

El libro está vinculado a un elemento de biblioteca genérico y contiene datos adicionales específicos de este tipo de material.

Atributos:
- elemento (ElementoBiblioteca): Referencia al elemento base de biblioteca.
- isbn (str): Código ISBN único del libro.
- numero_paginas (int): Número total de páginas del libro.
- genero (str): Género literario del libro (por ejemplo, 'Fantasía', 'Tecnología').
- editorial (str): Nombre de la editorial que publicó el libro.
    """
    elemento: ElementoBiblioteca = Reference()
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str
