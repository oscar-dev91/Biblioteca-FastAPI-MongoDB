from database import engine
from crud import elemento as crud_elemento

async def buscar_elemento_por_titulo_service(titulo: str):
    return await crud_elemento.buscar_elemento_por_titulo(titulo, engine)

async def listar_elementos_service():
    return await crud_elemento.listar_todos_los_elementos(engine)
