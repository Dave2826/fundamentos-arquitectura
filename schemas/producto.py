from pydantic import BaseModel, ConfigDict


class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class ProductoResponse(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)