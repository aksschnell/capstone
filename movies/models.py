from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    pass


class Genre(models.Model):
    name = models.CharField(default="", max_length=15)

    def __str__(self):
        return f"Genre name: {self.name}"


class Movie(models.Model):
    title = models.CharField(default="", max_length=100)
    image_url = models.CharField(default="", max_length=999)
    release_year = models.IntegerField(default=0, max_length=6)
    description = models.CharField(default="", max_length=9999)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genre")
    average_score = models.FloatField(default=-1, max_length=10)

 

    def serialize(self):
        return {
            "id": self.id,
            "title" : self.title,
            "image_url" : self.image_url,
            "release_year" : self.release_year,
            "description" : self.description,
            "genre" : self.genre.name,
            "average_score" : self.average_score
        }

class Review(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    likes_amount = models.IntegerField(default=0,max_length=999)
    dislikes_amount = models.IntegerField(default=0,max_length=999)
    content = models.CharField(default="", max_length=999)
    score = models.FloatField(default=0, max_length=99)


class Reaction(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.IntegerField(default=0, max_length=2)

