from fastapi import APIRouter, HTTPException
from models.elemento import ElementoBiblioteca
from services import elemento as elemento_service

router = APIRouter(prefix="/elementos", tags=["Elementos de Biblioteca"])

@router.get("/", response_model=list[ElementoBiblioteca])
async def listar_elementos():
    """
🔍 **Listar todos los elementos de la biblioteca**

Este endpoint devuelve una lista con todos los elementos disponibles en la biblioteca, incluyendo libros, revistas y DVDs.

📦 **Retorna**:
- Una lista de objetos `ElementoBiblioteca`.

❌ **Errores**:
- `404 Not Found`: Si no existen elementos registrados en la biblioteca.
"""
    elementos = await elemento_service.listar_elementos_service()
    if not elementos:
        raise HTTPException(status_code=404, detail="No hay elementos en la biblioteca")
    return elementos

@router.get("/buscar/{titulo}", response_model=list[ElementoBiblioteca])
async def buscar_por_titulo(titulo: str):
    """
🔍 **Buscar elementos por título**

Permite buscar todos los elementos de la biblioteca que coincidan con un título específico.

📥 **Parámetros**:
- `titulo` (*str*): El título del elemento a buscar.

📦 **Retorna**:
- Una lista de objetos `ElementoBiblioteca` que coincidan con el título.

❌ **Errores**:
- `404 Not Found`: Si no se encuentra ningún elemento con el título proporcionado.
"""
    elementos = await elemento_service.buscar_elemento_por_titulo_service(titulo)
    if not elementos:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return elementos
