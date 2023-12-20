from django.db import models

# Create your models here.
class Son(models.Model):
    number = models.IntegerField()
    count = models.BooleanField(default=True)
