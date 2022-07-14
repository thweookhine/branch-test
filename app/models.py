
from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=255)
    song_url = models.CharField(max_length=255)
    song_image = models.ImageField()
    song_data = models.FileField()
    song_lyrics = models.TextField()
    song_datetime = models.DateTimeField()

    def __str__(self):
        return self.song_title

