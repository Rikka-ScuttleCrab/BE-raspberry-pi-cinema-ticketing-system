import qrcode
import os
import json

from services.security_service import (
    generate_signature
)

QR_FOLDER = "static/qr"

os.makedirs(QR_FOLDER, exist_ok=True)


def generate_order_qr(order):

    sig = generate_signature(order.id)

    verify_url = (
        f"https://uncubic-mealy-yamileth.ngrok-free.dev"
        f"/api/v1/tickets/verify/"
        f"{order.id}"
        f"?sig={sig}"
    )

    qr_data = verify_url

    file_name = f"order_{order.id}.png"

    file_path = os.path.join(
        QR_FOLDER,
        file_name
    )

    absolute_path = os.path.abspath(
        file_path
    )

    qr = qrcode.make(qr_data)

    qr.save(absolute_path)

    return absolute_path