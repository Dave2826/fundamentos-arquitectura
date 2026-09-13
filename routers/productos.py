from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.producto import (
    ProductoCreate,
    ProductoResponse,
    ProductoUpdate
)
from services import producto_service


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.post(
    "",
    response_model=ProductoResponse
)
def crear_producto(
    producto: ProductoCreate,
    db: Session = Depends(get_db)
):
    return producto_service.crear_producto(
        db,
        producto
    )


@router.get(
    "",
    response_model=list[ProductoResponse]
)
def obtener_productos(
    db: Session = Depends(get_db)
):
    return producto_service.obtener_productos(db)


@router.get(
    "/disponibles",
    response_model=list[ProductoResponse]
)
def obtener_productos_disponibles(
    db: Session = Depends(get_db)
):
    return producto_service.obtener_productos_disponibles(db)


@router.get(
    "/{producto_id}",
    response_model=ProductoResponse
)
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    producto = producto_service.obtener_producto(
        db,
        producto_id
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.put(
    "/{producto_id}",
    response_model=ProductoResponse
)
def actualizar_producto(
    producto_id: int,
    producto_data: ProductoUpdate,
    db: Session = Depends(get_db)
):
    producto = producto_service.actualizar_producto(
        db,
        producto_id,
        producto_data
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    eliminado = producto_service.eliminar_producto(
        db,
        producto_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "mensaje": "Producto eliminado correctamente"
    }