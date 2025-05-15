from database import engine
from crud import elemento as crud_elemento

async def buscar_elemento_por_titulo_service(titulo: str):
    elementos = await crud_elemento.buscar_elemento_por_titulo(titulo, engine)
    if not elementos:
        raise ValueError('No se encontraron elementos con ese título')
    return elementos

async def listar_elementos_service():
    return await crud_elemento.listar_todos_los_elementos(engine)
