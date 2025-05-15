from fastapi import APIRouter, HTTPException
from models.elemento import ElementoBiblioteca
from services import elemento as elemento_service

router = APIRouter(prefix="/elementos", tags=["Elementos de Biblioteca"])

@router.get("/", response_model=list[ElementoBiblioteca])
async def listar_elementos():
    elementos = await elemento_service.listar_elementos_service()
    if not elementos:
        raise HTTPException(status_code=404, detail="No hay elementos en la biblioteca")
    return elementos

@router.get("/buscar/{titulo}", response_model=list[ElementoBiblioteca])
async def buscar_por_titulo(titulo: str):
    elementos = await elemento_service.buscar_elemento_por_titulo_service(titulo)
    if not elementos:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return elementos
