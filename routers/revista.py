from fastapi import APIRouter, HTTPException, status
from schemas.revista import RevistaCreate, RevistaOut
from services import revista as revista_service

router = APIRouter(prefix='/revistas', tags=['Revistas'])

@router.post('/', response_model=RevistaOut)
async def crear_revista(revista: RevistaCreate):
    """
    📘 **Crear una nueva revista**

    Registra una nueva revista con los datos suministrados.

    **Parámetros:**
    - `revista` (RevistaCreate): Datos de la revista.

    **Retorna:**
    - `RevistaOut`: Revista creada.
    """
    revista_creada = revista_service.crear_revista_service(revista)
    return RevistaOut.from_model(revista_creada)

@router.get('/', response_model=list[RevistaOut])
async def listar_revistas():
    """
    📚 **Listar todas las revistas**

    Muestra todas las revistas registradas.

    **Retorna:**
    - `list[RevistaOut]`: Lista de revistas.
    """
    revistas = await revista_service.listar_revistas_service()
    return [RevistaOut.from_model(revista) for revista in revistas]

@router.get('/buscar/id/{id}', response_model=RevistaOut)
async def buscar_revista_por_id(id: str):
    """
    🔎 **Buscar revista por ID**

    Recupera los datos de una revista específica usando su ID.

    **Parámetros:**
    - `id` (str): ID de la revista.

    **Retorna:**
    - `RevistaOut`: Revista encontrada.
    """
    revista = await revista_service.buscar_revista_por_id_service(id)
    if not revista:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return RevistaOut.from_model(revista)

@router.get('/buscar/titulo/{titulo}', response_model=list[RevistaOut])
async def buscar_revista_por_titulo(titulo: str):
    """
    🔍 **Buscar revistas por título**

    Filtra revistas que coincidan con el título dado.

    **Parámetros:**
    - `titulo` (str): Título a buscar.

    **Retorna:**
    - `list[RevistaOut]`: Resultados encontrados.
    """
    revistas = await revista_service.buscar_revista_por_titulo_service(titulo)
    if not revistas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontraron revistas con ese título')
    return [ RevistaOut.from_model(revista) for revista in revistas ]

@router.get('buscar/categoria/{categoria}', response_model=list[RevistaOut])
async def buscar_revista_por_categoria(categoria: str):
    """
    🗂️ **Buscar revistas por categoría**

    Filtra revistas asociadas a una categoría específica.

    **Parámetros:**
    - `categoria` (str): Categoría de la revista.

    **Retorna:**
    - `list[RevistaOut]`: Revistas encontradas.
    """
    revistas = await revista_service.buscar_revista_por_categoria_service(categoria)
    if not revistas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontraron revistas con esta categoría')
    return [ RevistaOut.from_model(revista) for revista in revistas ]

@router.put('/actualizar/{id}', response_model=RevistaOut)
async def actualizar_revista_por_id(id: str, revista: RevistaCreate):
    """
    📝 **Actualizar revista por ID**

    Modifica los datos de una revista existente.

    **Parámetros:**
    - `id` (str): ID de la revista.
    - `revista` (RevistaCreate): Datos nuevos.

    **Retorna:**
    - `RevistaOut`: Revista actualizada.
    """
    actualizado = await revista_service.actualizar_revista_por_id_service(id, revista)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return RevistaOut.from_model(actualizado)

@router.delete('eliminar/id/{id}')
async def eliminar_por_id(id: str):
    """
    ❌ **Eliminar revista por ID**

    Elimina la revista que coincida con el ID proporcionado.

    **Parámetros:**
    - `id` (str): ID de la revista.

    **Retorna:**
    - `dict`: Confirmación de eliminación.
    """
    eliminado = await revista_service.eliminar_revista_por_id_service(id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Revista no encontrada')
    return {'mensaje': 'Revista eliminada correctamente'}