from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from api.schemas.order import OrderRequest
from services.orderService import create_order_service, get_order_service
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
    
@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    try:
        data = get_order_service(db, order_id)

        if not data:
            return error_response(
                error_detail="Order not found",
                status_code=404
            )

        return success_response(
            data=data,
            message="GET ORDER SUCCESS"
        )
        
    except Exception as e:
        db.rollback()
        return error_response(str(e), status_code=500)