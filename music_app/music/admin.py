from django.contrib import admin
from .models import Artist, Album, Track, Genre, Playlist, RadioStation

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre')
    search_fields = ('name', 'genre')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year')
    search_fields = ('title', 'artist__name')
    list_filter = ('release_year', 'artist__name')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration')
    search_fields = ('title', 'album__title')
    list_filter = ('album__artist__name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')

admin.site.register(RadioStation)

# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('track', 'user', 'rating')
#     search_fields = ('track__title', 'user__username')
#     list_filter = ('rating',)