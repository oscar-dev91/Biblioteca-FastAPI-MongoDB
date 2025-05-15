from database import engine
from crud import libro as crud_libro
from schemas.libro import LibroCreate

async def crear_libro_service(libro_data: LibroCreate):
    return await crud_libro.crear_libro(libro_data, engine)

async def listar_libros_service():
    return await crud_libro.listar_libros(engine)

async def buscar_libro_por_titulo_service(titulo: str):
    return await crud_libro.buscar_por_titulo(titulo, engine)

async def buscar_libro_por_isbn_service(isbn: str):
    return await crud_libro.buscar_por_isbn(isbn, engine)

async def actualizar_libro_por_isbn_service(isbn: str, libro_data: LibroCreate):
    return await crud_libro.actualizar_libro_por_isbn(isbn, libro_data, engine)

async def eliminar_libro_por_isbn_service(isbn: str):
    return await crud_libro.eliminar_libro_por_isbn(isbn, engine)
