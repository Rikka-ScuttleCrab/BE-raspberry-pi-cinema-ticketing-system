from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from api.schemas.order import OrderRequest
from services.orderService import create_order_service
from api.response import success_response, error_response

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])

@router.post("/")
def post_order(data:OrderRequest, db: Session = Depends(get_db)):
    try:
        order = create_order_service(db, data)
        if isinstance(order, dict) and "error" in order:
            return error_response(order["error"], status_code=400)
            
        return success_response(
            data={
                "order_id": order["order_id"],
                "total_amount": int(order["total_amount"]),
                "tickets": order["tickets"]
            },
            message="ORDER SUCCESS"
        )
    except Exception as e:
        db.rollback()
        return error_response(str(e), status_code=500)