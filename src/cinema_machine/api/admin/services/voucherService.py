from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.others.voucher import Voucher

def get_all_vouchers_service(db: Session, page: int = 1, page_size: int = 30):

    offset = (page - 1) * page_size

    total = db.query(Voucher).count()
    
    vouchers = (
        db.query(Voucher)
        .order_by(Voucher.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    result = []

    for v in vouchers:

        result.append({
            "id": v.id,
            "voucher_code": v.voucher_code,
            "voucher_value": v.voucher_value,
            "voucher_exp": v.voucher_exp
        })

    return {
        "items": result,
        "total": total
    }
    
def create_voucher_admin_service(db: Session, data):

    existing = db.query(Voucher).filter(Voucher.voucher_code == data.voucher_code).first()

    if existing:
        raise ValueError("Voucher code already exists")

    try:
        voucher = Voucher(
            voucher_code=data.voucher_code,
            voucher_value=data.voucher_value,
            voucher_exp=data.voucher_exp
        )

        db.add(voucher)
        db.commit()
        db.refresh(voucher)

        return voucher

    except Exception:
        db.rollback()
        raise




def update_voucher_admin_service(db: Session, voucher_id: int, data):

    try:
        voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()

        if not voucher:
            return None

        update_data = data.model_dump(exclude_unset=True)

        if "voucher_code" in update_data:

            existing = db.query(Voucher).filter(
                func.lower(Voucher.voucher_code) == update_data["voucher_code"].lower(),
                Voucher.id != voucher_id
            ).first()

            if existing:
                raise ValueError("Voucher code already exists")

        for key in ["voucher_code", "voucher_value", "voucher_exp"]:
            if key in update_data:
                setattr(voucher, key, update_data[key])

        db.commit()
        db.refresh(voucher)

        return voucher

    except IntegrityError:
        db.rollback()
        raise ValueError("Voucher code already exists")

    except Exception:
        db.rollback()
        raise