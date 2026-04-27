from pydantic import BaseModel

class VoucherResponse(BaseModel):
    id: int
    voucher_value: str
    
    class Config:
        from_attributes = True