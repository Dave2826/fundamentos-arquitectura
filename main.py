from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import Producto


app = FastAPI(
    title="Fundamentos de Arquitectura - Backend",
    version="1.0.0"
)


# =========================
# Modelos de entrada
# =========================

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int


class ProductoUpdate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int


# =========================
# Rutas existentes
# =========================

@app.get("/")
def inicio():
    return {
        "mensaje": "Backend funcionando"
    }


@app.get("/alumno")
def obtener_alumno():
    return {
        "nombre": "David Morales",
        "carrera": "Desarrollo de Software",
        "semestre": 4
    }


@app.get("/contenedor")
def obtener_contenedor():
    return {
        "backend": "FastAPI",
        "contenedor": "Docker",
        "estado": "Aplicación funcionando dentro del contenedor"
    }


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola, {nombre}"
    }


@app.get("/sistema")
def obtener_sistema():
    return {
        "aplicacion": "Fundamentos de Arquitectura - Backend",
        "version": "1.0.0",
        "framework": "FastAPI",
        "ambiente": "Docker"
    }


# =========================
# CRUD Productos
# =========================

@app.post("/productos")
def crear_producto(
    producto: ProductoCreate,
    db: Session = Depends(get_db)
):
    nuevo_producto = Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        stock=producto.stock
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


@app.get("/productos")
def obtener_productos(
    db: Session = Depends(get_db)
):
    productos = db.query(Producto).all()

    return productos


@app.get("/productos/{producto_id}")
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    producto = db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@app.put("/productos/{producto_id}")
def actualizar_producto(
    producto_id: int,
    producto_data: ProductoUpdate,
    db: Session = Depends(get_db)
):
    producto = db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    producto.nombre = producto_data.nombre
    producto.descripcion = producto_data.descripcion
    producto.precio = producto_data.precio
    producto.stock = producto_data.stock

    db.commit()
    db.refresh(producto)

    return producto


@app.delete("/productos/{producto_id}")
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    producto = db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    db.delete(producto)
    db.commit()

    return {
        "mensaje": "Producto eliminado correctamente"
    }