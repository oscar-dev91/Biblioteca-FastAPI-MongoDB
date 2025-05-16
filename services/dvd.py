from database import engine
from crud import dvd as crud_dvd
from schemas.dvd import DVDCreate

async def crear_dvd_service(dvd_data: DVDCreate):
    """
Crea un nuevo DVD en el sistema.

Parámetros:
- dvd_data (DVDCreate): Datos del DVD a crear.

Retorna:
- DVD: El DVD creado.
"""
    return await crud_dvd.crear_dvd(dvd_data, engine)

async def listar_dvds_service():
    """
Lista todos los DVDs del sistema.

Retorna:
- List[DVD]: Lista de DVDs disponibles.
"""
    return await crud_dvd.listar_dvds(engine)

async def buscar_dvd_por_id_service(id: str):
    """
Busca un DVD por su ID.

Parámetros:
- id (str): ID del DVD.

Retorna:
- DVD: El DVD encontrado.

Errores:
- ValueError: Si no se encuentra el DVD.
"""
    dvd = await crud_dvd.buscar_por_id(id, engine)
    if not dvd:
        raise ValueError('No se encontró el DVD')
    return dvd

async def buscar_dvd_por_titulo_service(titulo: str):
    """
Busca DVDs por su título.

Parámetros:
- titulo (str): Título del DVD.

Retorna:
- List[DVD]: Lista de DVDs que coinciden con el título.

Errores:
- ValueError: Si no se encuentran DVDs con ese título.
"""
    dvds = await crud_dvd.buscar_por_titulo(titulo, engine)
    if not dvds:
        raise ValueError('No se encontraron DVDs con ese título')
    return dvds

async def buscar_dvd_por_genero_service(categoria: str):
    """
Busca DVDs por su categoría.

Parámetros:
- categoria (str): Categoría del DVD.

Retorna:
- List[DVD]: Lista de DVDs que coinciden con la categoría.

Errores:
- ValueError: Si no se encuentran DVDs con esa categoría.
"""
    dvds = await crud_dvd.buscar_por_genero(categoria, engine)
    if not dvds:
        raise ValueError('No se encontraron DVDs con ese genero')
    return dvds

async def actualizar_dvd_por_id_service(id: str, dvd_data: DVDCreate):
    """
Actualiza un DVD por su ID.

Parámetros:
- id (str): ID del DVD a actualizar.
- dvd_data (DVDCreate): Datos nuevos del DVD.

Retorna:
- DVD: El DVD actualizado.

Errores:
- ValueError: Si no se encuentra el DVD.
"""
    dvd = await crud_dvd.buscar_por_id(id, engine)
    if not dvd:
        raise ValueError('No se encontró el DVD')
    return await crud_dvd.actualizar_por_id(id, dvd_data, engine)

async def eliminar_por_id_service(id: str):
    """
Elimina un DVD por su ID.

Parámetros:
- id (str): ID del DVD a eliminar.

Retorna:
- bool: True si fue eliminado correctamente.

Errores:
- ValueError: Si no se encuentra el DVD.
"""
    dvd = await crud_dvd.buscar_por_id(id, engine)
    if not dvd:
        raise ValueError('No se encontró el DVD')
    return await crud_dvd.eliminar_por_id(id, engine)