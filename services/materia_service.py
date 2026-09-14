from sqlalchemy.orm import Session

from models.materia import Materia
from repositories import materia_repository
from schemas.materia import MateriaCreate, MateriaUpdate


def crear_materia(
    db: Session,
    materia_data: MateriaCreate
) -> Materia:
    nueva_materia = Materia(
        nombre=materia_data.nombre
    )

    return materia_repository.crear_materia(
        db,
        nueva_materia
    )


def obtener_materias(
    db: Session
) -> list[Materia]:
    return materia_repository.obtener_materias(db)


def obtener_materia(
    db: Session,
    materia_id: int
) -> Materia | None:
    return materia_repository.obtener_materia_por_id(
        db,
        materia_id
    )


def actualizar_materia(
    db: Session,
    materia_id: int,
    materia_data: MateriaUpdate
) -> Materia | None:
    materia = materia_repository.obtener_materia_por_id(
        db,
        materia_id
    )

    if materia is None:
        return None

    return materia_repository.actualizar_materia(
        db,
        materia,
        materia_data.nombre
    )


def eliminar_materia(
    db: Session,
    materia_id: int
) -> bool:
    materia = materia_repository.obtener_materia_por_id(
        db,
        materia_id
    )

    if materia is None:
        return False

    materia_repository.eliminar_materia(
        db,
        materia
    )

    return True