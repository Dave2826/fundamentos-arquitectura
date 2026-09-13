from fastapi import FastAPI

from routers import productos


app = FastAPI(
    title="Fundamentos de Arquitectura - Backend",
    version="1.0.0"
)


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


app.include_router(productos.router)