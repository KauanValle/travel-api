from django.core.exceptions import ObjectDoesNotExist
from functools import wraps

def handle_exceptions(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return 404, {'data': "This travel doesn't exist."}
        except Exception as e:
            print(e.args)
            return 500, {'data': "Internal server error, contact an administrator."}
        
    return wrapper