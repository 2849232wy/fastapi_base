from fastapi import Depends

from exception.ResponseException import ResponseException
from filters.filterAuth import TokenData, verify_token

def verify_is_teacher(tokenData: TokenData = Depends(verify_token)):
    if tokenData.type != 2:
        raise ResponseException(msg="权限不足", code=403)
    return tokenData