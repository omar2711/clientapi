from django.db import models

# Create your models here.

class server(models.Model):
    #user pid as key, totalSpace, usedSpace, freeSpace and time
    pid = models.CharField(max_length=100)
    totalSpace = models.IntegerField()
    usedSpace = models.IntegerField()
    freeSpace = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
