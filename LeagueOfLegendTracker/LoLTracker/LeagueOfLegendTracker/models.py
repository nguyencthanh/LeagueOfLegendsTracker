from django.db import models

# Create your models here.
class User(models.Model):
    puuid = models.CharField(max_length=255)
    gameName = models.CharField(max_length=255)
    tagLine = models.CharField(max_length=255)
    
    def __str__(self):
        return self.puuid