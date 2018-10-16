from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name
