from pydantic import BaseModel

class LibroCreate(BaseModel):
    """
Esquema de entrada para la creación de un nuevo libro.

Define los campos necesarios para registrar un libro en el sistema.

Atributos:
- titulo (str): Título del libro.
- autor (str): Nombre del autor del libro.
- ano_publicacion (int): Año en que se publicó el libro.
- isbn (str): Código ISBN del libro.
- numero_paginas (int): Total de páginas del libro.
- genero (str): Género literario del libro.
- editorial (str): Nombre de la editorial.
    """
    titulo: str
    autor: str
    ano_publicacion: int
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

class LibroOut(BaseModel):
    """
Esquema de salida que representa la información de un libro registrada en el sistema.

Incluye todos los campos del libro junto con su identificador único.

Atributos:
- id (str): Identificador único del libro.
- titulo (str): Título del libro.
- autor (str): Nombre del autor.
- ano_publicacion (int): Año de publicación.
- isbn (str): Código ISBN.
- numero_paginas (int): Total de páginas.
- genero (str): Género literario.
- editorial (str): Editorial del libro.
    """
    id: str
    titulo: str
    autor: str
    ano_publicacion: int
    isbn: str
    numero_paginas: int
    genero: str
    editorial: str

    class Config:
        from_attributes = True
        
    @classmethod
    def from_model(cls, libro):
        """
    Crea una instancia del esquema `LibroOut` a partir de un modelo de dominio completo.

    Este método de clase permite transformar un objeto de base de datos (por ejemplo, un documento
    de MongoDB u ORM) en una instancia del esquema de salida `LibroOut`, extrayendo tanto los
    atributos del propio objeto como los del objeto anidado `elemento`.

    Parámetros:
    - libro (Any): Objeto que representa un libro en el sistema, que incluye un atributo `elemento`
    - con los datos compartidos del recurso de biblioteca (título, autor, etc.).

    Retorna:
    - LibroOut: Instancia del esquema Pydantic con todos los campos listos para ser devueltos en la API.
    
    Ejemplo:
    - libro = await libro_service.obtener_libro()
    - libro_out = LibroOut.from_model(libro)
    """
        return cls(
            id=str(libro.id),
            titulo=libro.elemento.titulo,
            autor=libro.elemento.autor,
            ano_publicacion=libro.elemento.ano_publicacion,
            isbn=libro.isbn,
            numero_paginas=libro.numero_paginas,
            genero=libro.genero,
            editorial=libro.editorial
        )
