import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from starlette.requests import Request

from Student.urls import student_api
from Teacher.urls import teacher_api
from setting import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from filters.filterAuth import login_api
from exception.ResponseException import ResponseException
from filters.filterAuth import verify_token


app = FastAPI(dependencies=[Depends(verify_token)])
noAuth_app = FastAPI()
noAuth_app.include_router(router=student_api, prefix="/student")
noAuth_app.include_router(router=login_api)
noAuth_app.include_router(router=teacher_api, prefix="/teacher")
app.mount("", noAuth_app)

@app.exception_handler(ResponseException)
async def unicorn_exception_handler(request: Request, exc: ResponseException):
    return JSONResponse(
        status_code=exc.code,
        content={"msg": f"{exc.msg}", "code": exc.code},
    )
@noAuth_app.exception_handler(ResponseException)
async def unicorn_exception_handler(request: Request, exc: ResponseException):
    return JSONResponse(
        status_code=exc.code,
        content={"msg": f"{exc.msg}", "code": exc.code},
    )
# 注册 Tortoise-ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # 自动生成表结构
    add_exception_handlers=False,  # 添加异常处理器
)
if __name__ == '__main__':
    uvicorn.run(app="main:app", host='127.0.0.1', port=8000, reload=True)