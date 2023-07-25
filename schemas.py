# API Schemas

from pydantic import BaseModel


class ORMSchema(BaseModel):
    # Enable orm_mode by inherits this model
    class Config:
        orm_mode = True
