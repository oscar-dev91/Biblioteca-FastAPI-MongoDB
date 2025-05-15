from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
from models.dvd import DVD
from schemas.dvd import DVDCreate
import re

async def crear_dvd(dvd_data: DVDCreate, engine: AIOEngine):
    """
    Crea un nuevo DVD en el sistema.

    Registra un nuevo elemento de tipo "DVD" en la base de datos junto con sus características específicas.

    Parámetros:
    - dvd_data (DVDCreate): Datos del DVD a crear.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - DVD: Objeto DVD creado.
    """
    elemento = ElementoBiblioteca(
        titulo= dvd_data.titulo,
        autor= dvd_data.autor,
        ano_publicacion= dvd_data.ano_publicacion,
        tipo= "DVD"
    ) # type: ignore
    await engine.save(elemento)
    
    dvd = DVD(
        elemento= elemento,
        duracion= dvd_data.duracion,
        genero= dvd_data.duracion
    ) # type: ignore
    await engine.save(dvd)
    return dvd

async def listar_dvds(engine: AIOEngine):
    """
    Lista todos los DVDs registrados en el sistema.

    Parámetros:
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[DVD]: Lista de DVDs registrados.
    """
    return await engine.find(DVD)

async def buscar_por_titulo(titulo: str, engine: AIOEngine):
    """
    Busca DVDs cuyo título coincida total o parcialmente con el valor proporcionado.

    Parámetros:
    - titulo (str): Título a buscar.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[DVD]: Lista de DVDs encontrados.
    """
    regex = re.compile(f".*{re.escape(titulo)}.*", re.IGNORECASE)
    elementos = await engine.find(ElementoBiblioteca, {'titulo': {"$regex": regex}})
    if not elementos:
        return []
    #Extrayendo los ids de los elementos encontrados
    elemento_ids = [elemento.id for elemento in elementos]
    # Buscando DVDs de los elementos encontrados
    dvds = await engine.find(DVD, DVD.elemento.in_(elemento_ids))
    return dvds

async def buscar_por_categoria(categoria: str, engine: AIOEngine):
    """
    Busca DVDs por categoría.

    Parámetros:
    - categoria (str): Nombre de la categoría.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - List[DVD]: DVDs relacionados a la categoría.
    """
    regex = re.compile(f".*{re.escape(categoria)}.*", re.IGNORECASE)
    elementos = await engine.find(ElementoBiblioteca, {'categoria': {'$regex': regex}})
    if not elementos:
        return []
    elementos_ids = [elemento.id for elemento in elementos]
    dvds = await engine.find(DVD, DVD.elemento.in_(elementos_ids))
    return dvds

async def buscar_por_id(dvd_id: str, engine: AIOEngine):
    """
    Busca un DVD específico por su ID.

    Parámetros:
    - dvd_id (str): ID del DVD a buscar.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - DVD | None: DVD encontrado o None.
    """
    return await engine.find_one(DVD, DVD.id == dvd_id)

async def actualizar_por_id(dvd_id, dvd_data: DVDCreate, engine: AIOEngine):
    """
    Actualiza los datos de un DVD existente.

    Parámetros:
    - dvd_id (str): ID del DVD.
    - dvd_data (DVDCreate): Nuevos datos para actualizar.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - DVD | None: DVD actualizado o None si no existe.
    """
    dvd = await buscar_por_id(dvd_id, engine)
    if not dvd:
        return None
    
    dvd.elemento.titulo = dvd_data.titulo
    dvd.elemento.autor = dvd_data.autor
    dvd.elemento.ano_publicacion = dvd_data.ano_publicacion
    await engine.save(dvd.elemento)
    
    dvd.duracion = dvd_data.duracion
    dvd.genero = dvd_data.genero
    await engine.save(dvd)
    
    return dvd

async def eliminar_por_id(dvd_id: str, engine:AIOEngine):
    """
    Elimina un DVD por su ID.

    Elimina tanto el objeto DVD como su entrada asociada en ElementoBiblioteca.

    Parámetros:
    - dvd_id (str): ID del DVD.
    - engine (AIOEngine): Motor de base de datos.

    Retorna:
    - bool: True si se eliminó correctamente, False si no fue encontrado.
    """
    dvd = await buscar_por_id(dvd_id, engine)
    if not dvd:
        return False
    await engine.delete(dvd.elemento)
    await engine.delete(dvd)
    return True