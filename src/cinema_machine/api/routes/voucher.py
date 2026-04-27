from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from api.response import success_response, error_response
from api.schemas.voucher import VoucherResponse
from services.voucherService import validate_voucher_service

router = APIRouter(prefix="/api/v1/vouchers", tags=["Vouchers"])

@router.get("/validate")
def validate_voucher(voucher_code: str, db: Session = Depends(get_db)):
    result = validate_voucher_service(db, voucher_code)

    if "error" in result:
        return error_response(
            error_detail=result["error"],
            status_code=result["status_code"]
        )

    data = VoucherResponse.model_validate(result).model_dump(mode="json")

    return success_response(
        data=data,
        message="VOUCHER IS VALID"
    )