from pydantic import BaseModel

class RevistaCreate(BaseModel):
    """
Esquema de entrada para registrar una nueva revista en el sistema.

Contiene la información necesaria para crear una revista.

Atributos:
- titulo (str): Título de la revista.
- autor (str): Editor o responsable del contenido.
- ano_publicacion (int): Año de publicación.
- numero_edicion (int): Número de edición o volumen.
- categoria (str): Categoría temática de la revista.
    """
    titulo: str
    autor: str
    ano_publicacion: int
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
- ano_publicacion (int): Año de publicación.
- numero_edicion (int): Edición o volumen de la revista.
- categoria (str): Categoría temática.
    """
    id: str
    titulo: str
    autor: str
    ano_publicacion: int
    numero_edicion: int
    categoria: str
    
    class Config:
        from_attributes = True
        
    @classmethod
    def from_model(cls, revista):
        """
    Crea una instancia del esquema `RevistaOut` a partir de un modelo de dominio completo.

    Este método de clase permite convertir un objeto de base de datos que representa una revista
    en una instancia del esquema de salida `RevistaOut`, extrayendo tanto los atributos propios
    como los del objeto anidado `elemento`, que contiene información general del recurso.

    Parámetros:
    - revista (Any): Objeto que representa una revista en el sistema, con un atributo `elemento`
      que contiene datos comunes como título, autor y año de publicación.

    Retorna:
    - RevistaOut: Instancia del esquema Pydantic con todos los campos de la revista listos para ser devueltos en la API.
    
    Ejemplo:
    - revista = await revista_service.obtener_revista()
    - revista_out = RevistaOut.from_model(revista)
    """
        return cls(
            id=str(revista.id),
            titulo=revista.elemento.titulo,
            autor=revista.elemento.autor,
            ano_publicacion=revista.elemento.ano_publicacion,
            numero_edicion=revista.numero_edicion,
            categoria=revista.categoria
        )