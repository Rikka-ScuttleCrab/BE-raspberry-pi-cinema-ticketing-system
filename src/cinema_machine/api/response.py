from fastapi.responses import JSONResponse
import json
from fastapi.encoders import jsonable_encoder


def success_response(data: dict | list, message: str = "CALL API SUCCESS", status_code: int = 200):
    data_jsonable = jsonable_encoder(data)
    
    return JSONResponse(
        status_code=status_code,
        content={
            "error": None,
            "message": message,
            "data": data_jsonable,
            "status_code": status_code
        }
    )


def error_response(error_detail: str, message: str = "CALL API FAILED", status_code: int = 400):
    return JSONResponse(
        status_code=status_code,
        content=json.loads(json.dumps({
            "error": error_detail,
            "message": message,
            "data": None,
            "status_code": status_code
        }, indent=4))
    )