from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length = 100, blank = False)
    venue = models.TextField()
    poster_img = models.URLField()
    thumbnail_img = models.URLField()
    n_rounds = models.IntegerField(blank = True)
    description = models.TextField()
    rules = models.TextField()
    instructions = models.TextField()




