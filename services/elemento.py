from database import engine
from crud import elemento as crud_elemento

async def buscar_elemento_por_titulo_service(titulo: str):
    """
Busca elementos por su título.

Parámetros:
- titulo (str): Título del elemento.

Retorna:
- List[Elemento]: Lista de elementos encontrados.

Errores:
- ValueError: Si no se encuentran elementos con ese título.
"""
    elementos = await crud_elemento.buscar_elemento_por_titulo(titulo, engine)
    if not elementos:
        raise ValueError('No se encontraron elementos con ese título')
    return elementos

async def listar_elementos_service():
    """
Lista todos los elementos del sistema.

Retorna:
- List[Elemento]: Lista de todos los elementos.
"""
    return await crud_elemento.listar_todos_los_elementos(engine)
