from sqlalchemy.orm import Session

from models.producto import Producto
from repositories import producto_repository
from schemas.producto import ProductoCreate, ProductoUpdate


def crear_producto(
    db: Session,
    producto_data: ProductoCreate
) -> Producto:
    nuevo_producto = Producto(
        nombre=producto_data.nombre,
        descripcion=producto_data.descripcion,
        precio=producto_data.precio,
        stock=producto_data.stock
    )

    return producto_repository.crear_producto(
        db,
        nuevo_producto
    )


def obtener_productos(
    db: Session
) -> list[Producto]:
    return producto_repository.obtener_productos(db)


def obtener_producto(
    db: Session,
    producto_id: int
) -> Producto | None:
    return producto_repository.obtener_producto_por_id(
        db,
        producto_id
    )


def obtener_productos_disponibles(
    db: Session
) -> list[Producto]:
    return producto_repository.obtener_productos_disponibles(db)


def actualizar_producto(
    db: Session,
    producto_id: int,
    producto_data: ProductoUpdate
) -> Producto | None:
    producto = producto_repository.obtener_producto_por_id(
        db,
        producto_id
    )

    if producto is None:
        return None

    return producto_repository.actualizar_producto(
        db,
        producto,
        producto_data.nombre,
        producto_data.descripcion,
        producto_data.precio,
        producto_data.stock
    )


def eliminar_producto(
    db: Session,
    producto_id: int
) -> bool:
    producto = producto_repository.obtener_producto_por_id(
        db,
        producto_id
    )

    if producto is None:
        return False

    producto_repository.eliminar_producto(
        db,
        producto
    )

    return True