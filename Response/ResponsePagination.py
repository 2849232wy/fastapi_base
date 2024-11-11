from typing import Any

from pydantic import BaseModel
from typing_extensions import Optional

class Pagination(BaseModel):
    page: int = 1
    per_page: int = 10
    total: int = 0
    data: Optional[Any] = None

class ResponsePagination(BaseModel):
    """
    统一返回格式
    """
    code: int = 200
    msg: str = '成功'
    data: Optional[Pagination] = Pagination()
