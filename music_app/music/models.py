from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    youtube_id = models.CharField(max_length=100, blank=True)
    favorite_by_users = models.ManyToManyField(User, related_name="favorite_tracks", blank=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track, related_name='playlists')

    def __str__(self):
        return f"{self.name} by {self.user.username}"
    
class RadioStation(models.Model):
    name = models.CharField(max_length=100)
    stream_url = models.URLField()
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     track = models.ForeignKey(Track, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#     review = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.rating} by {self.user.username} for {self.track.title}"