from django.db import models

class MontyHallResult(models.Model):
    user_id = models.IntegerField()
    switched = models.BooleanField()
    won = models.BooleanField()