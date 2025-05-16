from pydantic import BaseModel

class DVDCreate(BaseModel):
    """
Esquema de entrada para la creación de un nuevo DVD.

Define los campos requeridos para registrar un DVD en el sistema.

Atributos:
- titulo (str): Título del DVD.
- autor (str): Director o creador del contenido.
- ano_publicacion (int): Año en que se publicó o produjo el DVD.
- duracion (int): Duración total del contenido en minutos.
- genero (str): Género del contenido del DVD.
    """
    titulo: str
    autor: str
    ano_publicacion: int
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
- ano_publicacion (int): Año de publicación o producción.
- duracion (int): Duración en minutos.
- genero (str): Género del contenido.
    """
    id: str
    titulo: str
    autor: str
    ano_publicacion: int
    duracion: int
    genero: str
    
    class Config:
        from_attributes = True
        
    @classmethod
    def from_model(cls, dvd):
        """
    Crea una instancia del esquema `DVDOut` a partir de un modelo de dominio completo.

    Este método de clase transforma un objeto de base de datos que representa un DVD en una
    instancia del esquema de salida `DVDOut`, extrayendo tanto los atributos propios como los
    del objeto anidado `elemento`, que contiene información general del recurso.

    Parámetros:
    - dvd (Any): Objeto que representa un DVD en el sistema, con un atributo `elemento`
      que incluye datos comunes como el título, autor y año de publicación.

    Retorna:
    - DVDOut: Instancia del esquema Pydantic con todos los campos del DVD listos para ser devueltos en la API.
    
    Ejemplo:
    - dvd = await dvd_service.obtener_dvd()
    - dvd_out = DVDOut.from_model(dvd)
    """
        return cls(
            id = str(dvd.id),
            titulo=dvd.elemento.titulo,
            autor=dvd.elemento.autor,
            ano_publicacion=dvd.elemento.ano_publicacion,
            duracion=dvd.duracion,
            genero=dvd.genero
        )