from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    website = models.URLField(max_length=100)    
    def __str__(self):
        return f"{self.name}"


class WatchList(models.Model):
    movie = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    is_active = models.BooleanField(default=True)    
    def __str__(self):
        return f"{self.movie}"

class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=100)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):       
        return f"{self.rating} | {self.description}" 
           