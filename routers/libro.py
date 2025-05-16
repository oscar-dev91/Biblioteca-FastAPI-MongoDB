from fastapi import APIRouter, HTTPException, status
from schemas.libro import LibroCreate, LibroOut
from services import libro as libro_service

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroOut)
async def crear_libro(libro: LibroCreate):
    """
    📚 **Crear un nuevo libro**

    Crea un nuevo registro de libro con la información proporcionada.

    **Parámetros:**
    - `libro` (LibroCreate): Datos del libro a registrar.

    **Retorna:**
    - `LibroOut`: Detalles del libro creado.
    """
    libro_creado = await libro_service.crear_libro_service(libro)
    return LibroOut.from_model(libro_creado)

@router.get("/", response_model=list[LibroOut])
async def listar_libros():
    """
    📚 **Listar todos los libros**

    Recupera la lista completa de libros registrados.

    **Retorna:**
    - `list[LibroOut]`: Lista de todos los libros disponibles.
    """
    libros = await libro_service.listar_libros_service()
    return [LibroOut.from_model(libro) for libro in libros]

@router.get("/buscar/titulo/{titulo}", response_model=list[LibroOut])
async def buscar_por_titulo(titulo: str):
    """
    🔍 **Buscar libros por título**

    Busca libros cuyo título coincida total o parcialmente con el valor proporcionado.

    **Parámetros:**
    - `titulo` (str): Título del libro a buscar.

    **Retorna:**
    - `list[LibroOut]`: Lista de libros que coinciden con el título.
    """
    libros = await libro_service.buscar_libro_por_titulo_service(titulo)
    if not libros:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron libros con ese título")
    return [LibroOut.from_model(libro) for libro in libros]

@router.get("/buscar/isbn/{isbn}", response_model=LibroOut)
async def buscar_por_isbn(isbn: str):
    """
    🔎 **Buscar libro por ISBN**

    Recupera un libro específico mediante su código ISBN.

    **Parámetros:**
    - `isbn` (str): ISBN del libro a buscar.

    **Retorna:**
    - `LibroOut`: Detalles del libro encontrado.
    """
    libro = await libro_service.buscar_libro_por_isbn_service(isbn)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return LibroOut.from_model(libro)

@router.put("/actualizar/{id}", response_model=LibroOut)
async def actualizar_por_id(id: str, libro: LibroCreate):
    """
    ✏️ **Actualizar un libro por ID**

    Actualiza los datos de un libro existente mediante su ID.

    **Parámetros:**
    - `id` (str): ID del libro a actualizar.
    - `libro` (LibroCreate): Nuevos datos del libro.

    **Retorna:**
    - `LibroOut`: Libro actualizado.
    """
    actualizado = await libro_service.actualizar_libro_por_id_service(id, libro)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return LibroOut.from_model(actualizado)

@router.delete("/eliminar/id/{id}")
async def eliminar_por_id(id: str):
    """
    🗑️ **Eliminar libro por ID**

    Elimina el libro correspondiente al ID proporcionado.

    **Parámetros:**
    - `id` (str): ID del libro a eliminar.

    **Retorna:**
    - `dict`: Mensaje de confirmación.
    """
    eliminado = await libro_service.eliminar_libro_por_id_service(id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}
