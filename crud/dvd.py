from odmantic import AIOEngine
from models.elemento import ElementoBiblioteca
from models.dvd import DVD
from schemas.dvd import DVDCreate
import re

async def crear_dvd(dvd_data: DVDCreate, engine: AIOEngine):
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
    return await engine.find(DVD)

async def buscar_por_titulo(titulo: str, engine: AIOEngine):
    regex = re.compile(f".*{re.escape(titulo)}.*", re.IGNORECASE)
    elementos = await engine.find(ElementoBiblioteca, {'titulo': {"$regex": regex}})
    if not elementos:
        return []
    #Extrayendo los ids de los elementos encontrados
    elemento_ids = [elemento.id for elemento in elementos]
    # Buscando DVDs de los elementos encontrados
    dvds = await engine.find(DVD, DVD.elemento.in_(elemento_ids))
    return dvds

