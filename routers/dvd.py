from fastapi import APIRouter, HTTPException, status
from schemas.dvd import DVDCreate, DVDOut
from services import dvd as dvd_service

router = APIRouter(prefix='/dvds', tags=["DVDs"])

@router.post('/', response_model=DVDOut)
async def crear_dvd(dvd: DVDCreate):
    """
    📀 **Crear un nuevo DVD**

    Registra un nuevo DVD con su información completa.

    **Parámetros:**
    - `dvd` (DVDCreate): Información del DVD.

    **Retorna:**
    - `DVDOut`: Detalles del DVD creado.
    """
    dvd_creado = await dvd_service.crear_dvd_service(dvd)
    return DVDOut(
        id=str(dvd_creado.id),
        titulo=dvd_creado.elemento.titulo,
        autor = dvd_creado.elemento.autor,
        ano_publicacion=dvd_creado.elemento.ano_publicacion,
        duracion= dvd_creado.duracion,
        genero= dvd_creado.genero
    )
    
@router.get('/', response_model=list[DVDOut])
async def listar_dvds():
    """
    📂 **Listar DVDs**

    Muestra todos los DVDs registrados en el sistema.

    **Retorna:**
    - `list[DVDOut]`: Colección de DVDs.
    """
    dvds = await dvd_service.listar_dvds_service()
    return [
        DVDOut(
        id=str(dvd.id),
        titulo=dvd.elemento.titulo,
        autor = dvd.elemento.autor,
        ano_publicacion=dvd.elemento.ano_publicacion,
        duracion= dvd.duracion,
        genero= dvd.genero
        ) for dvd in dvds
    ]
    
@router.get('/buscar/titulo/{titulo}', response_model=DVDOut)
async def buscar_por_titulo(titulo: str):
    """
    🔍 **Buscar DVD por título**

    Encuentra uno o varios DVDs que coincidan con el título dado.

    **Parámetros:**
    - `titulo` (str): Título del DVD.

    **Retorna:**
    - `list[DVDOut]`: Lista de DVDs encontrados.
    """
    dvds = await dvd_service.buscar_dvd_por_titulo_service(titulo)
    if not dvds:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron DVDs con ese título")
    return [
        DVDOut(
        id=str(dvd.id),
        titulo=dvd.elemento.titulo,
        autor = dvd.elemento.autor,
        ano_publicacion=dvd.elemento.ano_publicacion,
        duracion= dvd.duracion,
        genero= dvd.genero
        ) for dvd in dvds
    ]
    
@router.get('/buscar/categoria/{categoria}}', response_model=DVDOut)
async def buscar_por_categoria(categoria: str):
    """
    🗃️ **Buscar DVD por categoría**

    Muestra DVDs que pertenecen a una categoría específica.

    **Parámetros:**
    - `categoria` (str): Categoría del DVD.

    **Retorna:**
    - `list[DVDOut]`: DVDs encontrados en esa categoría.
    """
    dvds = await dvd_service.buscar_dvd_por_categoria_service(categoria)
    if not dvds:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DVDs no encontrado")
    return [
        DVDOut(
        id=str(dvd.id),
        titulo=dvd.elemento.titulo,
        autor = dvd.elemento.autor,
        ano_publicacion=dvd.elemento.ano_publicacion,
        duracion= dvd.duracion,
        genero= dvd.genero
        ) for dvd in dvds
    ]
    
@router.put('/actualizar/{id}', response_model=DVDOut)
async def actualizar_por_id(id:str, dvd: DVDCreate):
    """
    🛠️ **Actualizar un DVD**

    Modifica los datos de un DVD existente.

    **Parámetros:**
    - `id` (str): ID del DVD a actualizar.
    - `dvd` (DVDCreate): Nueva información.

    **Retorna:**
    - `DVDOut`: DVD actualizado.
    """
    actualizado = await dvd_service.actualizar_dvd_por_id_service(id, dvd)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DVD No encontrado')
    return DVDOut.from_model(actualizado)

@router.delete('/eliminar/id/{id}')
async def eliminar_por_id(id: str):
    """
    🧹 **Eliminar DVD**

    Elimina un DVD identificado por su ID.

    **Parámetros:**
    - `id` (str): ID del DVD.

    **Retorna:**
    - `dict`: Mensaje de confirmación.
    """
    eliminado = await dvd_service.eliminar_por_id_service(id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DVD no encontrado')
    return {'mensaje': 'DVD eliminado correctamente'}