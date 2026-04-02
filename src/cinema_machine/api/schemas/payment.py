from pydantic import BaseModel, Field
from typing import Optional


class PaymentCreateRequest(BaseModel):
    order_id: Optional[str] = Field(None, description="Client order identifier. If missing, backend will generate")
    amount: float = Field(..., gt=0, description="Amount in VND")
    order_info: Optional[str] = Field('Cinema ticket', description="Order description")
    order_type: Optional[str] = Field('other', description="Order type for VNPAY")
    bank_code: Optional[str] = Field('', description="Optional bank code")


class PaymentCreateResponse(BaseModel):
    order_id: str
    payment_url: str
    total_amount: float


class PaymentReturnResponse(BaseModel):
    success: bool
    response_code: str
    transaction_ref: str
    amount: float
    message: str
    params: dict
