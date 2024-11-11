from typing import Any

from pydantic import BaseModel
from typing_extensions import Optional


class ResponseModel(BaseModel):
    """
    统一返回格式
    """
    code: int = 200
    msg: str = '成功'
    data: Optional[Any] = None