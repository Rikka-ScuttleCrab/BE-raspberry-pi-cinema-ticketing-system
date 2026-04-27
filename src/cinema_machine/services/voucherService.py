from sqlalchemy.orm import Session
from datetime import date
from models.others.voucher import Voucher

def validate_voucher_service(db: Session, voucher_code: str):
    voucher = db.query(Voucher).filter(Voucher.voucher_code == voucher_code).first()

    # Trường hợp 1: Không tồn tại
    if not voucher:
        return {"error": "Voucher không tồn tại", "status_code": 404}

    # Trường hợp 2: Tồn tại nhưng đã hết hạn
    if voucher.voucher_exp < date.today():
        return {"error": "Voucher đã hết hạn sử dụng", "status_code": 400}

    # Trường hợp 3: Hợp lệ
    return {
        "id": voucher.id,
        "voucher_value": voucher.voucher_value
    }