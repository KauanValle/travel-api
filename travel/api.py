from ninja import Router
from .schemas import TravelSchema
from .models import Travel
from .excepions import handle_exceptions

travel_router = Router()

@travel_router.post('/', response={201: dict, 500: dict})
def create_travel(request, travel_schema: TravelSchema):
    try: 
        user_id = getattr(request, 'user_id', None)
        travel = Travel(user_id_id=user_id, **travel_schema.dict())
        travel.save()
        return 201, {'data': travel_schema.dict()}
    except Exception:
        return 500, {'data': 'Internal server error, contact administrator.'}

@travel_router.get('/all', response={200: dict})
def show_all_travels(request):
    results = list(Travel.objects.all().filter(user_id=request.user_id).values("id", "starting_from", "arriving_in", "starting_from_datetime", "arriving_in_datetime", "finished"))
    return {'data': results}

@travel_router.get('/{travel_id}', response={200: dict, 404: dict, 500: dict})
@handle_exceptions
def show_travel_by_id(request, travel_id: int):
    result = Travel.objects.filter(id=travel_id, user_id=request.user_id).values(
        "id", "starting_from", "arriving_in", "starting_from_datetime", "arriving_in_datetime", "finished"
    ).first()

    return 200, {'data': result}

@travel_router.put('/{travel_id}', response={200: dict, 404: dict, 500: dict})
@handle_exceptions
def update_travel(request, travel_schema:TravelSchema, travel_id: int):
    travel = Travel.objects.get(id=travel_id, user_id=request.user_id)

    for field, value in travel_schema.dict().items():
        if hasattr(travel, field):
            setattr(travel, field, value)

    travel.save()
    return 200, {'data': travel_schema.dict()}

@travel_router.delete('/{travel_id}', response={200: dict, 404: dict, 500: dict})
@handle_exceptions
def delete_travel(request, travel_id: int):
    travel = Travel.objects.get(id=travel_id, user_id=request.user_id)
    travel.delete()

    return 200, {'data': 'Travel has deleted with success'}

@travel_router.post('/finish-travel/{travel_id}', response={200: dict, 404: dict, 500: dict})
@handle_exceptions
def finish_travel(request, travel_id: int):
    travel = Travel.objects.get(id=travel_id, user_id=request.user_id)
    travel.finish_travel()

    return 200, {'data': 'Travel has been finished'}