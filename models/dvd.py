from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class DVD(Model):
    elemento: ElementoBiblioteca = Reference()
    duracion: int
    genero: str