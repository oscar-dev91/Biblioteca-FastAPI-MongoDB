from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
from models.libro import Libro
from schemas.libro import LibroCreate
import re

async def crear_libro(libro_data: LibroCreate, engine: AIOEngine):
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
    return await engine.find(Libro)

async def buscar_por_titulo(titulo: str, engine: AIOEngine):
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
    return await engine.find_one(Libro, Libro.isbn == isbn)

async def actualizar_libro_por_isbn(isbn: str, libro_data: LibroCreate, engine: AIOEngine):
    libro = await buscar_por_isbn(isbn, engine)
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

async def eliminar_libro_por_isbn(isbn: str, engine: AIOEngine):
    libro = await buscar_por_isbn(isbn, engine)
    if not libro:
        return False
    await engine.delete(libro)
    await engine.delete(libro.elemento)
    return True
