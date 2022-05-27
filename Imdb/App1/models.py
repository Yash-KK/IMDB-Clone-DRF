from django.db import models

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
       
        