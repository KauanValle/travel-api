from django.db import models
from users.models import Users

class Travel(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    starting_from = models.CharField(max_length=40)
    arriving_in = models.CharField(max_length=40)
    starting_from_datetime = models.DateField()
    arriving_in_datetime = models.DateField()
    finished = models.BooleanField()

    def finish_travel(self):
        self.finished = True
        self.save()

    class Meta:
        db_table = 'travel'

