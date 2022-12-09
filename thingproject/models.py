from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    
    name = models.CharField(max_length = 30, unique = True, blank=False)
    description = models.CharField(max_length = 120, blank = True, unique=False)
    quanity = models.IntegerField(
        unique=False, 
        validators=[MaxValueValidator(100),
            MinValueValidator(1) 
            ]
        )
    
    