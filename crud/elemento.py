from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
import re

async def buscar_elemento_por_titulo(titulo: str, engine: AIOEngine):
    regex = re.compile(f".*{re.escape(titulo)}.*", re.IGNORECASE)
    return await engine.find(ElementoBiblioteca, {'titulo': {"$regex": regex}})

async def listar_todos_los_elementos(engine: AIOEngine):
    return await engine.find(ElementoBiblioteca)
