from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
from models.revista import Revista
from schemas.revista import RevistaCreate
from bson import ObjectId
import re

async def crear_revista(revista_data: RevistaCreate, engine: AIOEngine):
    """
    Crea una nueva revista en el sistema.

    Registra un nuevo elemento de tipo "Revista" junto con sus datos específicos.

    Parámetros:
    - revista_data (RevistaCreate): Datos de la revista.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - Revista: Revista creada exitosamente.
    """
    elemento = ElementoBiblioteca(
        titulo = revista_data.titulo,
        autor = revista_data.autor,
        ano_publicacion= revista_data.ano_publicacion,
        tipo="Revista"
    ) # type: ignore
    await engine.save(elemento)
    
    revista = Revista(
        elemento=elemento,
        numero_edicion= revista_data.numero_edicion,
        categoria= revista_data.categoria
    ) # type: ignore
    await engine.save(revista)
    return revista

async def listar_revistas(engine: AIOEngine):
    """
    Lista todas las revistas registradas en el sistema.

    Parámetros:
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[Revista]: Lista de revistas.
    """
    return await engine.find(Revista)

async def buscar_por_titulo(titulo: str, engine: AIOEngine):
    """
    Busca revistas cuyo título coincida total o parcialmente.

    Parámetros:
    - titulo (str): Título o fragmento del título.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[Revista]: Revistas encontradas.
    """
    regex = re.compile(f".*{re.escape(titulo)}.*", re.IGNORECASE)
    elementos = await engine.find(ElementoBiblioteca, {'titulo': {"$regex": regex}})
    if not elementos:
        return []
    elementos_ids = [elemento.id for elemento in elementos]
    revistas = await engine.find(Revista, Revista.elemento.in_(elementos_ids))
    return revistas

async def buscar_por_categoria(categoria: str, engine: AIOEngine):
    """
    Busca revistas por categoría.

    Parámetros:
    - categoria (str): Categoría a buscar.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[Revista]: Lista de revistas que coinciden.
    """
    regex = re.compile(f".*{re.escape(categoria)}.*", re.IGNORECASE)
    revistas = await engine.find(Revista, {'categoria': {"$regex": regex}})
    if not revistas:
        return []
    
    return revistas

async def buscar_por_id(revista_id: str, engine: AIOEngine):
    """
    Busca una revista por su identificador único.

    Parámetros:
    - revista_id (str): ID de la revista.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - Revista | None: Revista encontrada o None.
    """
    return await engine.find_one(Revista, Revista.id == ObjectId(revista_id))

async def actualizar_por_id(revista_id: str, revista_data: RevistaCreate, engine: AIOEngine):
    """
    Actualiza los datos de una revista existente.

    Parámetros:
    - revista_id (str): ID de la revista.
    - revista_data (RevistaCreate): Datos nuevos.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - Revista | None: Revista actualizada o None si no fue encontrada.
    """
    revista = await buscar_por_id(revista_id, engine)
    if not revista:
        return None
    
    revista.elemento.titulo = revista_data.titulo
    revista.elemento.autor = revista_data.autor
    revista.elemento.ano_publicacion = revista_data.ano_publicacion
    await engine.save(revista.elemento)
    
    revista.categoria = revista_data.categoria
    revista.numero_edicion = revista_data.numero_edicion
    await engine.save(revista)
    return revista

async def eliminar_revista_por_id(revista_id: str, engine: AIOEngine):
    """
    Elimina una revista del sistema junto con su elemento asociado.

    Parámetros:
    - revista_id (str): ID de la revista.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - bool: True si fue eliminada correctamente, False si no existe.
    """
    revista = await buscar_por_id(revista_id, engine)
    if not revista:
        return False
    await engine.delete(revista)
    await engine.delete(revista.elemento)
    return True