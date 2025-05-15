from fastapi import APIRouter, HTTPException
from schemas.libro import LibroCreate, LibroOut
from services import libro as libro_service

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroOut)
async def crear_libro(libro: LibroCreate):
    libro_creado = await libro_service.crear_libro_service(libro)
    return LibroOut(
        id=str(libro_creado.id),
        titulo=libro_creado.elemento.titulo,
        autor=libro_creado.elemento.autor,
        ano_publicacion=libro_creado.elemento.ano_publicacion,
        isbn=libro_creado.isbn,
        numero_paginas=libro_creado.numero_paginas,
        genero=libro_creado.genero,
        editorial=libro_creado.editorial
    )

@router.get("/", response_model=list[LibroOut])
async def listar_libros():
    libros = await libro_service.listar_libros_service()
    return [
        LibroOut(
            id=str(libro.id),
            titulo=libro.elemento.titulo,
            autor=libro.elemento.autor,
            ano_publicacion=libro.elemento.ano_publicacion,
            isbn=libro.isbn,
            numero_paginas=libro.numero_paginas,
            genero=libro.genero,
            editorial=libro.editorial
        ) for libro in libros
    ]

@router.get("/buscar/titulo/{titulo}", response_model=list[LibroOut])
async def buscar_por_titulo(titulo: str):
    libros = await libro_service.buscar_libro_por_titulo_service(titulo)
    if not libros:
        raise HTTPException(status_code=404, detail="No se encontraron libros con ese título")
    return [
        LibroOut(
            id=str(libro.id),
            titulo=libro.elemento.titulo,
            autor=libro.elemento.autor,
            ano_publicacion=libro.elemento.ano_publicacion,
            isbn=libro.isbn,
            numero_paginas=libro.numero_paginas,
            genero=libro.genero,
            editorial=libro.editorial
        ) for libro in libros
    ]

@router.get("/buscar/isbn/{isbn}", response_model=LibroOut)
async def buscar_por_isbn(isbn: str):
    libro = await libro_service.buscar_libro_por_isbn_service(isbn)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return LibroOut(
        id=str(libro.id),
        titulo=libro.elemento.titulo,
        autor=libro.elemento.autor,
        ano_publicacion=libro.elemento.ano_publicacion,
        isbn=libro.isbn,
        numero_paginas=libro.numero_paginas,
        genero=libro.genero,
        editorial=libro.editorial
    )

@router.put("/actualizar/isbn/{isbn}", response_model=LibroOut)
async def actualizar_por_isbn(isbn: str, libro: LibroCreate):
    actualizado = await libro_service.actualizar_libro_por_isbn_service(isbn, libro)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return LibroOut(
        id=str(actualizado.id),
        titulo=actualizado.elemento.titulo,
        autor=actualizado.elemento.autor,
        ano_publicacion=actualizado.elemento.ano_publicacion,
        isbn=actualizado.isbn,
        numero_paginas=actualizado.numero_paginas,
        genero=actualizado.genero,
        editorial=actualizado.editorial
    )

@router.delete("/eliminar/isbn/{isbn}")
async def eliminar_por_isbn(isbn: str):
    eliminado = await libro_service.eliminar_libro_por_isbn_service(isbn)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}
