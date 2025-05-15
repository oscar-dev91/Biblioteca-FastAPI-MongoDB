from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class Revista(Model):
    """
Modelo que representa una revista en la biblioteca.

La revista se enlaza con un elemento de biblioteca común y contiene información específica como su número de edición y categoría temática.

Atributos:
- elemento (ElementoBiblioteca): Referencia al elemento base de biblioteca.
- numero_edicion (int): Número de edición o volumen de la revista.
- categoria (str): Nombre de la categoría a la que pertenece la revista (ej. Ciencia, Moda, Tecnología).
    """
    elemento: ElementoBiblioteca = Reference()
    numero_edicion: int
    categoria: str