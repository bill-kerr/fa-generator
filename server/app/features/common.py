from pydantic import BaseModel


class Identifiable(BaseModel):
    id: int

    class Config:
        orm_mode = True
