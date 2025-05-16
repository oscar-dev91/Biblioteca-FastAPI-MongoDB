from database import engine
from crud import revista as crud_revista
from schemas.revista import RevistaCreate

async def crear_revista_service(revista_data: RevistaCreate):
    """
Crea una nueva revista en el sistema.

Parámetros:
- revista_data (RevistaCreate): Datos de la revista a crear.

Retorna:
- Revista: La revista creada.
"""
    return await crud_revista.crear_revista(revista_data, engine) # type: ignore

async def listar_revistas_service():
    """
Lista todas las revistas del sistema.

Retorna:
- List[Revista]: Lista de revistas disponibles.
"""
    return await crud_revista.listar_revistas(engine)

async def buscar_revista_por_id_service(id: str):
    """
Busca una revista por su ID.

Parámetros:
- id (str): ID de la revista.

Retorna:
- Revista: La revista encontrada.

Errores:
- ValueError: Si no se encuentra la revista.
"""
    revista = crud_revista.buscar_por_id(id, engine)
    if not revista:
        raise ValueError('No se encontró esta revista')
    return revista

async def buscar_revista_por_titulo_service(titulo: str):
    """
Busca revistas por su título.

Parámetros:
- titulo (str): Título de la revista.

Retorna:
- List[Revista]: Lista de revistas que coinciden con el título.

Errores:
- ValueError: Si no se encuentran revistas con ese título.
"""

    revistas = await crud_revista.buscar_por_titulo(titulo, engine)
    if not revistas:
        raise ValueError('No se encontraron revistas con ese titulo')
    return revistas

async def buscar_revista_por_categoria_service(categoria: str):
    """
Busca revistas por su categoría.

Parámetros:
- categoria (str): Categoría de la revista.

Retorna:
- List[Revista]: Lista de revistas que coinciden con la categoría.

Errores:
- ValueError: Si no se encuentran revistas con esa categoría.
"""

    revistas = await crud_revista.buscar_por_categoria(categoria, engine)
    if not revistas:
        raise ValueError('No se encontraron revistas con esa categoría')
    return revistas

async def actualizar_revista_por_id_service(id: str, revista_data: RevistaCreate):
    """
Actualiza una revista por su ID.

Parámetros:
- id (str): ID de la revista.
- revista_data (RevistaCreate): Datos nuevos de la revista.

Retorna:
- Revista: La revista actualizada.

Errores:
- ValueError: Si no se encuentra la revista.
"""

    revista = crud_revista.buscar_por_id(id, engine)
    if not revista:
        raise ValueError('No se encontró esta revista')
    return await crud_revista.actualizar_por_id(id, revista_data, engine)

async def eliminar_revista_por_id_service(id: str):
    """
Elimina una revista del sistema junto con su elemento asociado.

Parámetros:
- id (str): ID de la revista.

Retorna:
- bool: True si fue eliminada correctamente.

Errores:
- ValueError: Si no se encuentra la revista.
    """
    revista = crud_revista.buscar_por_id(id, engine)
    if not revista:
        raise ValueError('No se encontró esta revista')
    return await crud_revista.eliminar_revista_por_id(id, engine)