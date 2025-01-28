from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    token_autenticate = models.CharField(max_length=30, null=True, blank=True, default=None)

    class Meta:
        db_table = 'users'


