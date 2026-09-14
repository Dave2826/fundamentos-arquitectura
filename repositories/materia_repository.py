from sqlalchemy.orm import Session

from models.materia import Materia


def crear_materia(
    db: Session,
    materia: Materia
) -> Materia:
    db.add(materia)
    db.commit()
    db.refresh(materia)

    return materia


def obtener_materias(
    db: Session
) -> list[Materia]:
    return db.query(Materia).all()


def obtener_materia_por_id(
    db: Session,
    materia_id: int
) -> Materia | None:
    return (
        db.query(Materia)
        .filter(Materia.id == materia_id)
        .first()
    )


def actualizar_materia(
    db: Session,
    materia: Materia,
    nombre: str
) -> Materia:
    materia.nombre = nombre

    db.commit()
    db.refresh(materia)

    return materia


def eliminar_materia(
    db: Session,
    materia: Materia
) -> None:
    db.delete(materia)
    db.commit()