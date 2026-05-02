import hmac
import hashlib
from api.payment.config import CHECKSUM_KEY


def verify_signature(data: dict, received_signature: str) -> bool:
    data_copy = data.copy()
    data_copy.pop("signature", None)

    sorted_items = sorted(data_copy.items())

    raw = "&".join(f"{k}={v}" for k, v in sorted_items)

    generated_signature = hmac.new(
        CHECKSUM_KEY.encode(),
        raw.encode(),
        hashlib.sha256
    ).hexdigest()

    print("RAW:", raw)
    print("GEN SIGN:", generated_signature)
    print("RECEIVED:", received_signature)

    return generated_signature == received_signature