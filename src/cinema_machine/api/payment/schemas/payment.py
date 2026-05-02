from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    amount: int = Field(..., gt=0, description="Số tiền > 0")