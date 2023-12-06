from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=20)
    actor=models.CharField(max_length=20)
    actress=models.CharField(max_length=20)
    rating=models.IntegerField()
    release_date=models.DateField()
