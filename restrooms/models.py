from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Toilet(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    cleanliness=models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    purchase=models.BooleanField()