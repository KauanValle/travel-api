import secrets
from ninja import Router
from .schemas import UserSchema, GetTokenSchema
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from .exceptions import user_not_exist_exception

users_router = Router()

@users_router.post('/', response={201: dict, 401: dict, 500: dict}, tags=["Users"])
def create_user(request, user_schema: UserSchema):
    exists_user = exists_user_by_email(user_schema.email)
    if not exists_user:
        user_schema.token_autenticate = generate_token()
        user_schema.password = make_password(user_schema.password)
        user = Users(**user_schema.dict())
        user.save()
    else:
        return 401, {'data': 'The user already exists in the system.'}

    return 201, {'data': user_schema.dict()}
    
@users_router.post('/get-token', response={200: dict, 404: dict, 500: dict}, tags=["Users"])
@user_not_exist_exception
def get_user_token(request, get_token_schema: GetTokenSchema):
    email = get_token_schema.email
    user = Users.objects.get(email=email)
    password = check_password(get_token_schema.password, user.password)
    if password:
        return {'data': {'token': user.token_autenticate}}
    
    return {'data': 'Wrong password. Try again with a correctly password.'}

def exists_user_by_email(email_user):
    try:
        Users.objects.get(email=email_user)
        return True
    except Exception as e:
        return False
    
def generate_token():
    return secrets.token_hex(16)