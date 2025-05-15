from pydantic import BaseModel

class DVDCreate(BaseModel):
    """
Esquema de entrada para la creación de un nuevo DVD.

Define los campos requeridos para registrar un DVD en el sistema.

Atributos:
- titulo (str): Título del DVD.
- autor (str): Director o creador del contenido.
- ano_publicacion (str): Año en que se publicó o produjo el DVD.
- duracion (int): Duración total del contenido en minutos.
- genero (str): Género del contenido del DVD.
    """
    titulo: str
    autor: str
    ano_publicacion: str
    duracion: int
    genero: str
    
class DVDOut(BaseModel):
    """
Esquema de salida que representa un DVD registrado en el sistema.

Incluye los datos del DVD junto con su identificador único.

Atributos:
- id (str): Identificador único del DVD.
- titulo (str): Título del DVD.
- autor (str): Creador o director.
- ano_publicacion (str): Año de publicación o producción.
- duracion (int): Duración en minutos.
- genero (str): Género del contenido.
    """
    id: str
    titulo: str
    autor: str
    ano_publicacion: str
    duracion: int
    genero: str
    
    class Config:
        from_attributes = True