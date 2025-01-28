from ninja import Schema
from .models import Users

class UserSchema(Schema):
    first_name: str
    email: str
    username: str
    password: str
    token_autenticate: str = None

class GetTokenSchema(Schema):
    email: str
    password: str