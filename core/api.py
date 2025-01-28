from ninja import NinjaAPI
from travel.api import travel_router
from users.api import users_router

api = NinjaAPI(title="Travel API", version="1.0", description="Documentação da API de viagens")
api.add_router('travel/', travel_router)
api.add_router('users/', users_router)