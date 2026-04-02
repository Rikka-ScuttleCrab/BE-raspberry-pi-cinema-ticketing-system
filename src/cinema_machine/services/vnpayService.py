import hashlib
import hmac
import os
import urllib.parse
import random
from datetime import datetime, timedelta

from config.databaseConfig import settings

VNPAY_URL = os.environ.get('VNPAY_URL', settings.VNPAY_URL)
VNPAY_TMN_CODE = os.environ.get('VNPAY_TMN_CODE', settings.VNPAY_TMN_CODE)
VNPAY_HASH_SECRET = os.environ.get('VNPAY_HASH_SECRET', settings.VNPAY_HASH_SECRET)
VNPAY_RETURN_URL = os.environ.get('VNPAY_RETURN_URL', 'http://localhost:5000/api/v1/payments/return')


def build_vnpay_url(order_id: str, amount: int, ip_addr: str, order_info: str = 'Cinema ticket', order_type: str = 'other', bank_code: str = '') -> str:
    amount_100 = int(amount * 100)
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    expire = (datetime.now() + timedelta(minutes=15)).strftime('%Y%m%d%H%M%S')

    params = {
        'vnp_Version': '2.1.0',
        'vnp_Command': 'pay',
        'vnp_TmnCode': VNPAY_TMN_CODE,
        'vnp_Amount': str(amount_100),
        'vnp_CurrCode': 'VND',
        'vnp_TxnRef': order_id,
        'vnp_OrderInfo': order_info,
        'vnp_OrderType': order_type,
        'vnp_Locale': 'vn',
        'vnp_ReturnUrl': VNPAY_RETURN_URL,
        'vnp_IpAddr': ip_addr,
        'vnp_CreateDate': now,
        'vnp_ExpireDate': expire
    }

    if bank_code:
        params['vnp_BankCode'] = bank_code

    sorted_keys = sorted(params.keys())
    hash_data = '&'.join(f"{key}={params[key]}" for key in sorted_keys)
    secure_hash = hmac.new(VNPAY_HASH_SECRET.encode('utf-8'), hash_data.encode('utf-8'), hashlib.sha512).hexdigest()

    params['vnp_SecureHash'] = secure_hash
    query_string = urllib.parse.urlencode(params)

    return f"{VNPAY_URL}?{query_string}"


def verify_vnpay_return(query_params: dict) -> tuple[bool, dict]:
    query = query_params.copy()
    vnp_secure_hash = query.pop('vnp_SecureHash', None)
    query.pop('vnp_SecureHashType', None)

    sorted_keys = sorted(k for k in query.keys() if k.startswith('vnp_'))
    hash_data = '&'.join(f"{k}={query[k]}" for k in sorted_keys)
    calculated_hash = hmac.new(VNPAY_HASH_SECRET.encode('utf-8'), hash_data.encode('utf-8'), hashlib.sha512).hexdigest()

    if calculated_hash != (vnp_secure_hash or '').lower():
        return False, {'message': 'Invalid secure hash'}

    response_code = query.get('vnp_ResponseCode')
    success = response_code == '00'

    return True, {
        'success': success,
        'response_code': response_code,
        'transaction_ref': query.get('vnp_TxnRef'),
        'amount': int(query.get('vnp_Amount', 0)) / 100,
        'message': 'Payment successful' if success else 'Payment failed',
        'params': query
    }

