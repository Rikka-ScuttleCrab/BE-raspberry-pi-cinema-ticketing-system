import hmac
import hashlib

from config.security import SECRET_ROLE_KEY


def generate_signature(order_id: int):

    message = str(order_id)

    signature = hmac.new(

        SECRET_ROLE_KEY.encode(),

        message.encode(),

        hashlib.sha256

    ).hexdigest()

    return signature