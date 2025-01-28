from ninja import ModelSchema
from .models import Travel

class TravelSchema(ModelSchema):
    class Meta:
        model = Travel
        fields = [
            'starting_from',
            'arriving_in',
            'starting_from_datetime',
            'arriving_in_datetime',
            'finished'
        ]