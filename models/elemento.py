from odmantic import Model

class ElementoBiblioteca(Model):
    """
Modelo base que representa un elemento de la biblioteca.

Este modelo define los atributos comunes a todos los tipos de materiales disponibles en la biblioteca,
como libros, DVDs y revistas.

Atributos:
- titulo (str): Título del material.
- autor (str): Nombre del autor o creador del material.
- ano_publicacion (int): Año en que fue publicado o producido.
- tipo (str): Tipo de elemento. Puede ser 'Libro', 'DVD' o 'Revista'.
    """
    titulo: str
    autor: str
    ano_publicacion: int
    tipo: str  # Puede ser 'Libro', 'DVD', 'Revista'
