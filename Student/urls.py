
from typing import Optional
import uuid

from fastapi import  APIRouter, Body
from fastapi.params import Depends
from pydantic import BaseModel

from Response.ResponseModel import ResponseModel
from Student.models import Student
from filters.filterAuth import get_password_hash


student_api = APIRouter()

class RegisterStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: str
    password: str
    teacher_id: Optional[int] = None


@student_api.post("/register")
async def register_student(register_info: RegisterStudent = Body(..., description="学生注册信息", Depends=[])):
    # 先生成一个uuid
    student = register_info.__dict__

    student['sno'] = uuid.uuid4()
    student.update({"password": get_password_hash(password=student['password'])})
    await Student.create(**student)
    return ResponseModel()