from secrets import token_hex


class Config:
    SECRET_KEY = token_hex(16)
    