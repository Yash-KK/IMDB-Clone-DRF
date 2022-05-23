from django.db import models

# Create your models here.
class Movie(models.Model):
    movie = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.movie}"