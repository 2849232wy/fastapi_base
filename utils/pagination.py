from email.policy import default
from typing import Dict
from fastapi import Query

from pydantic import BaseModel, Field


class QueryPagination(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=10, ge=10)

class ReturnPagination(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=10, ge=10)
    offset: int = Field(default=0)

def get_page_params(query: QueryPagination = Query()):
    """
    获取分页参数
    :param page: 页码
    :param size: 每页数量
    :return: (offset, limit)
    """
    offset = (query.page - 1) * query.limit
    return ReturnPagination(page=query.page, limit=query.limit, offset=offset)
