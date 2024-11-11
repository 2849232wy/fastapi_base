from typing import Optional

from datetime import datetime, timedelta, timezone

import jwt
from fastapi.security.utils import get_authorization_scheme_param

from dbmodels.models import Teacher, Student

from fastapi import Depends, APIRouter, Body
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from typing_extensions import Annotated
from exception.ResponseException import ResponseException
from Response.ResponseModel import ResponseModel
from pydantic import Field
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca257879793f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 360
from starlette.requests import Request
class MyOAuth2PasswordBearer(OAuth2PasswordBearer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise ResponseException(
                    code=401,
                    msg="请先登录"
                )
            else:
                return None
        return param


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    type: Optional[int] = None



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = MyOAuth2PasswordBearer(tokenUrl="token")

login_api = APIRouter()


# 校验盐加密密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 获取hash密码
def get_password_hash(password):
    return pwd_context.hash(password)


# 创建token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": int(expire.timestamp())})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class LoginClass(BaseModel):
    email: str = Field(description="用户邮箱" )
    password: str = Field(description="用户密码")
    type: int = Field(description="用户类型:1-用户，2-教师")


# 验证token
async def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = ResponseException(
        code=401,
        msg="无效的token"
    )
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        tokenData:TokenData = TokenData()
        tokenData.id = payload.get("id")
        tokenData.type = payload.get("type")
        if id is None:
            raise ResponseException(code=500, msg="用户不存在")

        return tokenData
    except InvalidTokenError:
        raise credentials_exception





@login_api.post("/login", summary="用户登录")
async def login_for_access_token(
    data: LoginClass = Body(..., description="用户登录信息")
) -> ResponseModel:
    user = None
    if data.type == 1:
        user = await Student.get_or_none(email=data.email)
    elif data.type == 2:
        user = await Teacher.get_or_none(email=data.email)
    if not user:
        raise ResponseException(code=400, msg='用户不存在')
    if not verify_password(data.password, user.password):
        raise ResponseException(code=400, msg='密码错误')
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"id": user.id, "type": data.type}, expires_delta=access_token_expires
    )
    return ResponseModel(data={
        "access_token": access_token,
        "token_type": "bearer",
    })





