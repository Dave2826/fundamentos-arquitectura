from sqlalchemy.orm import Session

from models.producto import Producto


def crear_producto(db: Session, producto: Producto) -> Producto:
    db.add(producto)
    db.commit()
    db.refresh(producto)

    return producto


def obtener_productos(db: Session) -> list[Producto]:
    return db.query(Producto).all()


def obtener_producto_por_id(
    db: Session,
    producto_id: int
) -> Producto | None:
    return (
        db.query(Producto)
        .filter(Producto.id == producto_id)
        .first()
    )


def obtener_productos_disponibles(
    db: Session
) -> list[Producto]:
    return (
        db.query(Producto)
        .filter(Producto.stock > 0)
        .all()
    )


def actualizar_producto(
    db: Session,
    producto: Producto,
    nombre: str,
    descripcion: str,
    precio: float,
    stock: int
) -> Producto:
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock

    db.commit()
    db.refresh(producto)

    return producto


def eliminar_producto(
    db: Session,
    producto: Producto
) -> None:
    db.delete(producto)
    db.commit()