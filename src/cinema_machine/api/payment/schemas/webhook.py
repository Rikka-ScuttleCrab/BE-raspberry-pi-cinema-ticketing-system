from pydantic import BaseModel
from typing import Optional

class PayOSWebhookData(BaseModel):
    orderCode: int
    amount: int
    description: Optional[str]
    status: str
    signature: str