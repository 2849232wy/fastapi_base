from typing import Optional

from fastapi import APIRouter, Query
from fastapi.params import Depends
from fastapi_pagination.ext.tortoise import paginate
from typing_extensions import Annotated
from fastapi_pagination import Page, paginate
from Response.ResponseModel import ResponseModel
from Response.ResponsePagination import Pagination, ResponsePagination
from major.models import *
from exception.ResponseException import ResponseException
from filters.filterAuth import TokenData
from dbmodels.models import Major
from filters.common import verify_is_teacher
from utils.pagination import get_page_params, ReturnPagination

major_api = APIRouter()


@major_api.get("/major", summary="获取所有专业", dependencies=[Depends(verify_is_teacher)])
async def get_major(pagination: Annotated[ReturnPagination, Depends(get_page_params)], query: MajorQueryDTO = Query(default=None)):
    """
    获取所有专业
    """
    if not query:
        query = MajorQueryDTO()
    query = { k+"__contains": v for k,v in query.__dict__.items() if v is not None}
    data = await Major.filter(**query).offset(pagination.offset).limit(pagination.limit).all().values(id="id", name="name")
    total = await Major.filter(**query).all().count()
    ReturnPagination = Pagination(data=data, page=pagination.page, per_page=pagination.limit, total=total)
    return ResponsePagination(data=ReturnPagination)



@major_api.post("/major", summary="添加专业", dependencies=[Depends(verify_is_teacher)])
async def add_major( major: MajorAddVO):
    """
    添加专业
    """
    await Major.create(**major.__dict__)
    return ResponseModel()

@major_api.delete("/major/{major_id}", summary="删除专业", dependencies=[Depends(verify_is_teacher)])
async def delete_major(major_id: int):
    """
    删除专业
    """
    await Major.filter(id=major_id).delete()
    return ResponseModel()


@major_api.put("/major", summary="修改专业", dependencies=[Depends(verify_is_teacher)])
async def edit_major(major: MajorEditVO):
    """
    修改专业
    """
    await Major.filter(id=major.id).update(**major.__dict__)
    return ResponseModel()


