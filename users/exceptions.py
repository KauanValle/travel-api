from functools import wraps
from django.core.exceptions import ObjectDoesNotExist

def user_not_exist_exception(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return 404, {'data': "This user doesn't exist."}
        except Exception as e:
            return 500, {'data': "Internal server error, contact an administrator."}
        
    return wrapper