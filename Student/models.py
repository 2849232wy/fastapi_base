from pydantic import BaseModel
from typing_extensions import Optional

class RegisterStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: str
    password: str
    teacher_id: Optional[int] = None