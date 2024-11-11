import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination
from starlette.requests import Request

from Student.urls import student_api
from Teacher.urls import teacher_api
from setting import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from filters.filterAuth import login_api
from exception.ResponseException import ResponseException
from filters.filterAuth import verify_token
from major.urls import major_api
from fastapi.openapi.utils import get_openapi

app = FastAPI(dependencies=[Depends(verify_token)])
noAuth_app = FastAPI()
noAuth_app.include_router(router=student_api, prefix="/student", tags=["学生"])
noAuth_app.include_router(router=login_api, tags=["登录"])
noAuth_app.include_router(router=teacher_api, prefix="/teacher", tags=["教师"])

app.include_router(router=major_api, tags=["专业"])
# 合并 OpenAPI 文档
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Main App",
#         version="1.0.0",
#         routes=app.routes,
#     )
#     noauth_openapi_schema = get_openapi(
#         title="No Auth App",
#         version="1.0.0",
#         routes=noAuth_app.routes,
#     )
#     openapi_schema["paths"].update(noauth_openapi_schema["paths"])
#     openapi_schema["components"]["schemas"].update(noauth_openapi_schema["components"]["schemas"])
#     app.openapi_schema = openapi_schema
#     return openapi_schema
#
# app.openapi = custom_openapi
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