from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class Libro(Model):
    elemento: ElementoBiblioteca = Reference()
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str
