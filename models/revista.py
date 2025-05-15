from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class Revista(Model):
    elemento: ElementoBiblioteca = Reference()
    numero_edicion: int
    categoria: int