from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca

async def buscar_elemento_por_titulo(titulo: str, engine: AIOEngine):
    return await engine.find(ElementoBiblioteca, ElementoBiblioteca.titulo == titulo)

async def listar_todos_los_elementos(engine: AIOEngine):
    return await engine.find(ElementoBiblioteca)
