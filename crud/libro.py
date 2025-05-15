from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
from models.libro import Libro
from schemas.libro import LibroCreate
import re

async def crear_libro(libro_data: LibroCreate, engine: AIOEngine):
    """
    Crea un nuevo libro en el sistema.

    Registra un nuevo elemento de tipo "Libro" en la base de datos, incluyendo su información
    general y los detalles específicos del libro.

    Parámetros:
    - libro_data (LibroCreate): Datos del libro a crear.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - Libro: Objeto del libro creado.
    """
    elemento = ElementoBiblioteca(
        titulo=libro_data.titulo,
        autor=libro_data.autor,
        ano_publicacion=libro_data.ano_publicacion,
        tipo="Libro"
    ) # type: ignore
    await engine.save(elemento)

    libro = Libro(
        elemento=elemento,
        isbn=libro_data.isbn,
        numero_paginas=libro_data.numero_paginas,
        genero=libro_data.genero,
        editorial=libro_data.editorial
    ) # type: ignore
    await engine.save(libro)
    return libro

async def listar_libros(engine: AIOEngine):
    """
    Lista todos los libros registrados en el sistema.

    Parámetros:
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - List[Libro]: Lista de libros encontrados.
    """
    return await engine.find(Libro)

async def buscar_por_titulo(titulo: str, engine: AIOEngine):
    """
    Busca libros por título utilizando coincidencias parciales y sin distinguir mayúsculas.

    Parámetros:
    - titulo (str): Título o fragmento del título del libro.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - List[Libro]: Libros coincidentes.
    """
    regex = re.compile(f".*{re.escape(titulo)}.*", re.IGNORECASE)
    elementos = await engine.find(ElementoBiblioteca, {'titulo': {"$regex": regex}})

    if not elementos:
        return []

    # Extraer IDs de los elementos encontrados
    elemento_ids = [elemento.id for elemento in elementos]

    # Buscar libros que referencian esos elementos
    libros = await engine.find(Libro, Libro.elemento.in_(elemento_ids))
    return libros

async def buscar_por_isbn(isbn: str, engine: AIOEngine):
    """
    Busca un libro específico por su ISBN.

    Parámetros:
    - isbn (str): Código ISBN del libro.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - Libro | None: Libro encontrado o None si no existe.
    """
    return await engine.find_one(Libro, Libro.isbn == isbn)

async def buscar_por_id(libro_id: str, engine: AIOEngine):
    """
    Busca un libro específico por su ID.

    Parámetros:
    - libro_id (str): Identificador único del libro.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - Libro | None: Libro encontrado o None si no existe.
    """
    return await engine.find_one(Libro, Libro.id == libro_id)

async def actualizar_libro_por_id(libro_id: str, libro_data: LibroCreate, engine: AIOEngine):
    """
    Actualiza los datos de un libro existente usando su ID.

    Parámetros:
    - libro_id (str): ID del libro a actualizar.
    - libro_data (LibroCreate): Nuevos datos del libro.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - Libro | None: Libro actualizado o None si no se encontró.
    """
    libro = await buscar_por_id(libro_id, engine)
    if not libro:
        return None

    libro.elemento.titulo = libro_data.titulo
    libro.elemento.autor = libro_data.autor
    libro.elemento.ano_publicacion = libro_data.ano_publicacion
    await engine.save(libro.elemento)

    libro.isbn = libro_data.isbn
    libro.numero_paginas = libro_data.numero_paginas
    libro.genero = libro_data.genero
    libro.editorial = libro_data.editorial
    await engine.save(libro)

    return libro

async def eliminar_libro_por_id(libro_id: str, engine: AIOEngine):
    """
    Elimina un libro del sistema junto con su información relacionada como elemento.

    Parámetros:
    - libro_id (str): ID del libro a eliminar.
    - engine (AIOEngine): Instancia del motor de base de datos ODMantic.

    Retorna:
    - bool: True si fue eliminado exitosamente, False si no se encontró.
    """
    libro = await buscar_por_id(libro_id, engine)
    if not libro:
        return False
    await engine.delete(libro)
    await engine.delete(libro.elemento)
    return True
