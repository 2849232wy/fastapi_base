
from typing import Optional
import uuid

from fastapi import  APIRouter, Body
from pydantic import BaseModel

from Response.ResponseModel import ResponseModel
from dbmodels.models import Teacher
from exception.ResponseException import ResponseException
from filters.filterAuth import get_password_hash


teacher_api = APIRouter()

class RegisterTeacher(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: str
    password: str


@teacher_api.post("/register", description="老师注册")
async def register_student(register_info: RegisterTeacher = Body(..., description="老师注册信息")):
    choose_teacher = await Teacher.get_or_none(email=register_info.email)
    if(choose_teacher):
        raise ResponseException(msg='邮箱已存在', code=400)
    # 先生成一个uuid
    teacher = register_info.__dict__
    teacher['tno'] = uuid.uuid4()
    teacher.update({"password": get_password_hash(password=teacher['password'])})
    await Teacher.create(**teacher)
    return ResponseModel()