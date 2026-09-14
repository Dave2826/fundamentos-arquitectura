from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.materia import (
    MateriaCreate,
    MateriaResponse,
    MateriaUpdate
)
from services import materia_service


router = APIRouter(
    prefix="/materias",
    tags=["Materias"]
)


@router.post(
    "",
    response_model=MateriaResponse
)
def crear_materia(
    materia: MateriaCreate,
    db: Session = Depends(get_db)
):
    return materia_service.crear_materia(
        db,
        materia
    )


@router.get(
    "",
    response_model=list[MateriaResponse]
)
def obtener_materias(
    db: Session = Depends(get_db)
):
    return materia_service.obtener_materias(db)


@router.get(
    "/{materia_id}",
    response_model=MateriaResponse
)
def obtener_materia(
    materia_id: int,
    db: Session = Depends(get_db)
):
    materia = materia_service.obtener_materia(
        db,
        materia_id
    )

    if materia is None:
        raise HTTPException(
            status_code=404,
            detail="Materia no encontrada"
        )

    return materia


@router.put(
    "/{materia_id}",
    response_model=MateriaResponse
)
def actualizar_materia(
    materia_id: int,
    materia_data: MateriaUpdate,
    db: Session = Depends(get_db)
):
    materia = materia_service.actualizar_materia(
        db,
        materia_id,
        materia_data
    )

    if materia is None:
        raise HTTPException(
            status_code=404,
            detail="Materia no encontrada"
        )

    return materia


@router.delete("/{materia_id}")
def eliminar_materia(
    materia_id: int,
    db: Session = Depends(get_db)
):
    eliminado = materia_service.eliminar_materia(
        db,
        materia_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Materia no encontrada"
        )

    return {
        "mensaje": "Materia eliminada correctamente"
    }