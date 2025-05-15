from pydantic import BaseModel

class RevistaCreate(BaseModel):
    """
Esquema de entrada para registrar una nueva revista en el sistema.

Contiene la información necesaria para crear una revista.

Atributos:
- titulo (str): Título de la revista.
- autor (str): Editor o responsable del contenido.
- ano_publicacion (str): Año de publicación.
- numero_edicion (int): Número de edición o volumen.
- categoria (str): Categoría temática de la revista.
    """
    titulo: str
    autor: str
    ano_publicacion: str
    numero_edicion: int
    categoria: str
    
class RevistaOut(BaseModel):
    """
Esquema de salida que representa una revista registrada en el sistema.

Incluye todos los detalles de la revista junto con su ID.

Atributos:
- id (str): Identificador único de la revista.
- titulo (str): Título de la revista.
- autor (str): Editor o creador del contenido.
- ano_publicacion (str): Año de publicación.
- numero_edicion (int): Edición o volumen de la revista.
- categoria (str): Categoría temática.
    """
    id: str
    titulo: str
    autor: str
    ano_publicacion: str
    numero_edicion: int
    categoria: str
    
    class Config:
        from_attributes = True