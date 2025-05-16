from database import engine
from crud import libro as crud_libro
from schemas.libro import LibroCreate

async def crear_libro_service(libro_data: LibroCreate):
    """
Crea un nuevo libro en el sistema.

Parámetros:
- libro_data (LibroCreate): Datos del libro a crear.

Retorna:
- Libro: El libro creado.
"""
    return await crud_libro.crear_libro(libro_data, engine)

async def listar_libros_service():
    """
Lista todos los libros del sistema.

Retorna:
- List[Libro]: Lista de libros disponibles.
"""
    return await crud_libro.listar_libros(engine)

async def buscar_libro_por_id_service(id: str):
    """
Busca un libro por su ID.

Parámetros:
- id (str): ID del libro.

Retorna:
- Libro: El libro encontrado.

Errores:
- ValueError: Si no se encuentra el libro.
"""
    libro = await crud_libro.buscar_por_id(id, engine)
    if not libro:
        raise ValueError('No se encontró el libro')
    return libro

async def buscar_libro_por_titulo_service(titulo: str):
    """
Busca libros por su título.

Parámetros:
- titulo (str): Título del libro.

Retorna:
- List[Libro]: Lista de libros que coinciden con el título.

Errores:
- ValueError: Si no se encuentran libros con ese título.
"""
    libros = await crud_libro.buscar_por_titulo(titulo, engine)
    if not libros:
        raise ValueError('No se encontraron libros con ese título')
    return libros

async def buscar_libro_por_isbn_service(isbn: str):
    """
Busca un libro por su ISBN.

Parámetros:
- isbn (str): ISBN del libro.

Retorna:
- Libro: El libro encontrado.

Errores:
- ValueError: Si no se encuentra el libro.
"""
    libro = await crud_libro.buscar_por_isbn(isbn, engine)
    if not libro:
        raise ValueError('No se encontró el libro')
    return libro

async def actualizar_libro_por_id_service(id: str, libro_data: LibroCreate):
    """
Actualiza un libro por su ID.

Parámetros:
- id (str): ID del libro a actualizar.
- libro_data (LibroCreate): Datos nuevos del libro.

Retorna:
- Libro: El libro actualizado.

Errores:
- ValueError: Si no se encuentra el libro.
"""
    libro = await crud_libro.buscar_por_id(id, engine)
    if not libro:
        raise ValueError('No se encontró el libro')
    return await crud_libro.actualizar_libro_por_id(id, libro_data, engine)

async def eliminar_libro_por_id_service(id: str):
    """
Elimina un libro por su ID.

Parámetros:
- id (str): ID del libro a eliminar.

Retorna:
- bool: True si fue eliminado correctamente.

Errores:
- ValueError: Si no se encuentra el libro.
"""
    libro = await crud_libro.buscar_por_id(id, engine)
    if not libro:
        raise ValueError('No se encontró el libro')
    return await crud_libro.eliminar_libro_por_id(id, engine)
