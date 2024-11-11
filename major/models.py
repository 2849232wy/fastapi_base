from typing import Optional

from pydantic import BaseModel

class MajorPO(BaseModel):
    id: int
    name: str

class MajorAddVO(BaseModel):
    name: str

class MajorEditVO(BaseModel):
    id: int
    name: str

class MajorQueryDTO(BaseModel):
    name: Optional[str] = None