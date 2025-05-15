from odmantic import Model

class ElementoBiblioteca(Model):
    titulo: str
    autor: str
    ano_publicacion: int
    tipo: str  # Puede ser 'Libro', 'DVD', 'Revista'
