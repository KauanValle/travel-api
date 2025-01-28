import re
from django.http import JsonResponse
from users.models import Users


class TokenAutenticateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.target_routes = [r'^/api/travel/']

    def __call__(self, request):
        if any(re.match(pattern, request.path) for pattern in self.target_routes):
            token =  request.headers.get('token-autenticate')
            if not token:
                return JsonResponse({'data': 'Token has not specified'})
                
            user_id = Users.objects.get(token_autenticate=token)
            request.user_id = user_id.id
            
        response = self.get_response(request)
        return response