import math
from core.security.role import has_role
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.response import success_response, error_response
from api.deps import get_db, get_current_user_token
from api.admin.schemas.voucher import (
    VoucherAdminResponse,
    VoucherCreateAdmin,
    VoucherUpdateAdmin
)

from api.admin.services.voucherService import (
    get_all_vouchers_service,
    create_voucher_admin_service,
    update_voucher_admin_service
)

router = APIRouter(prefix="/vouchers", tags=["Vouchers"])

@router.get("/")
def get_all_vouchers(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    raw = get_all_vouchers_service(db, page=page)

    items = [
        VoucherAdminResponse.model_validate(m).model_dump(mode="json")
        for m in raw["items"]
    ]

    page_size = 30
    total = raw["total"]
    total_pages = math.ceil(total / page_size)

    return success_response(
        data={
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages,
            "items": items,
        },
        message="GET ALL VOUCHERS SUCCESS"
    )
    
@router.post("/")
def create_voucher(
    payload: VoucherCreateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        voucher = create_voucher_admin_service(db, payload)

        return success_response(
            data={"id": voucher.id},
            message="CREATE VOUCHER SUCCESS",
            status_code=201
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)


@router.put("/{voucher_id}")
def update_voucher(
    voucher_id: int,
    payload: VoucherUpdateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        voucher = update_voucher_admin_service(db, voucher_id, payload)

        if not voucher:
            return error_response("Voucher not found", status_code=404)

        return success_response(
            data={"id": voucher.id},
            message="UPDATE VOUCHER SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)