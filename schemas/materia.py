from pydantic import BaseModel, ConfigDict


class MateriaBase(BaseModel):
    nombre: str


class MateriaCreate(MateriaBase):
    pass


class MateriaUpdate(MateriaBase):
    pass


class MateriaResponse(MateriaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)