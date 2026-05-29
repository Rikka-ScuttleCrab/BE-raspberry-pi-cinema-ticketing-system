import hmac
import hashlib
import requests
import datetime
import time
from fastapi import HTTPException
from models.tickets.order import Order
from sqlalchemy.orm import Session
from api.payment.utils.verify import verify_signature
from api.payment.config import CHECKSUM_KEY, API_KEY, CLIENT_ID, PAYOS_URL


def create_payment_link(order_id: int, amount: int, db: Session):
    
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(404, "Order not found")
    
    order_code = int(time.time() * 1000)
    
    order.payment_order_code = order_code
    db.commit()
    data = {
        "orderCode": order_code,
        "amount": amount,
        "description": "",
        "cancelUrl": "http://localhost:3000/cancel",
        "returnUrl": "http://localhost:3000/success",
    }

    data_to_sign = {
    "amount": data["amount"],
    "cancelUrl": data["cancelUrl"],
    "description": data["description"],
    "orderCode": data["orderCode"],
    "returnUrl": data["returnUrl"],
    }

    raw = build_raw_string(data_to_sign)

    signature = hmac.new(
        CHECKSUM_KEY.encode(),
        raw.encode(),
        hashlib.sha256
    ).hexdigest()

    data["signature"] = signature

    headers = {
        "x-client-id": CLIENT_ID,
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    res = requests.post(PAYOS_URL, json=data, headers=headers)

    print("RAW:", raw)  # debug
    print("SIGN:", signature)
    print("RES:", res.text)

    return res.json()

def get_payment_status_from_payos(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order or not order.payment_order_code:
        raise HTTPException(404, "Order not found or chưa tạo payment")

    url = PAYOS_URL + f"/{order.payment_order_code}"

    headers = {
        "x-client-id": CLIENT_ID,
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    res = requests.get(url, headers=headers)

    print("STATUS RES:", res.text)

    return res.json()

def process_payment_webhook(payload: dict, db: Session):
    print("WEBHOOK RAW:", payload)

    data = payload.get("data", {})

    order_code = data.get("orderCode")
    payos_code = data.get("code") or payload.get("code")

    print("ORDER CODE:", order_code)
    print("PAYOS CODE:", payos_code)
    
    
    if not order_code:
        return {"message": "Missing orderCode"}

    order = db.query(Order).filter(
        Order.payment_order_code == order_code
    ).first()

    if not order:
        print("❌ Order not found in DB")
        return {"message": "Order not found"}

    print("DB order_code:", order.payment_order_code)
    print("Webhook order_code:", order_code)
    
    # idempotent
    if order.status == "PAID":
        return {"message": "Already processed"}

    if payos_code == "00":
        order.status = "PAID"
        order.paid_at = datetime.datetime.utcnow()

        for ticket in order.tickets:
            ticket.status = "CONFIRMED"

    else:
        order.status = "FAILED"

    db.commit()

    print("✅ UPDATED ORDER:", order.id)

    return {"message": "OK"}



def build_raw_string(data: dict) -> str:
    sorted_items = sorted(data.items())
    return "&".join(f"{k}={v}" for k, v in sorted_items)