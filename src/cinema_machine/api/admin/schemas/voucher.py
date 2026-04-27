from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class VoucherAdminResponse(BaseModel):
    id: int
    voucher_code: str
    voucher_value: str
    voucher_exp: date

    class Config:
        from_attributes = True
        
        
class VoucherCreateAdmin(BaseModel):
    voucher_code: str
    voucher_value: str
    voucher_exp: date




class VoucherUpdateAdmin(BaseModel):
    voucher_code: str
    voucher_value: str
    voucher_exp: date
