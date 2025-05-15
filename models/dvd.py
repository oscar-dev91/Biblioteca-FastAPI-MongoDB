from odmantic import Model, Reference
from models.elemento import ElementoBiblioteca

class DVD(Model):
    """
Modelo que representa un DVD como material disponible en la biblioteca.

El DVD se asocia a un elemento general de biblioteca y contiene información específica sobre su duración y género.

Atributos:
- elemento (ElementoBiblioteca): Referencia al elemento de biblioteca asociado.
- duracion (int): Duración del DVD en minutos.
- genero (str): Género del contenido del DVD (por ejemplo, 'Documental', 'Drama').
    """
    elemento: ElementoBiblioteca = Reference()
    duracion: int
    genero: str