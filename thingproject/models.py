from django.db import models

class Thing(models.Model):
    
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100, blank = False)
    quanity = models.IntegerField(blank = False)
    
    