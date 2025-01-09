from typing import TypeVar, TypedDict, List

D = TypeVar("D")

RespData = TypedDict("RespData",{"success": bool,"data": List[D]})

Errors = TypedDict("Errors",{"code": int,"message": str})

RespError = TypedDict("RespError",{"success": bool,"error": Errors})

