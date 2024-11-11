
from typing import Optional
import uuid

from fastapi import APIRouter, Body, Path
from pydantic import BaseModel

from Response.ResponseModel import ResponseModel
from dbmodels.models import Student
from filters.filterAuth import get_password_hash
from Student.models import RegisterStudent

student_api = APIRouter()




@student_api.post("/register", summary="学生注册")
async def register_student(register_info: RegisterStudent = Body(..., description="学生注册信息", Depends=[])):
    # 先生成一个uuid
    student = register_info.__dict__
    student['sno'] = uuid.uuid4()
    student.update({"password": get_password_hash(password=student['password'])})
    await Student.create(**student)
    return ResponseModel()

@student_api.put("/course/{course_id}", summary="学生选课")
async def choose_course(course_id: int = Path()):
    return ResponseModel()