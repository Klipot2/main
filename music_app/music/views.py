from django.shortcuts import render, redirect
from .models import Track, Album, Artist, Playlist

def index(request):
    query = request.GET.get('query', '')
    context = {'query': query}  # Добавляем query в контекст для использования в шаблоне
    
    if query:
        context['tracks'] = Track.objects.filter(title__icontains=query)
        context['albums'] = Album.objects.filter(title__icontains=query)
        context['artists'] = Artist.objects.filter(name__icontains=query)
    
    return render(request, 'music/home.html', context)

def search(request):
    query = request.GET.get('query', '')
    if not query:
        return render(request, 'search_results.html', {'tracks': [], 'albums': [], 'artists': []})

    tracks = Track.objects.filter(title__icontains=query)
    albums = Album.objects.filter(title__icontains=query)
    artists = Artist.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {
        'tracks': tracks,
        'albums': albums,
        'artists': artists,
    })

def add_to_favorites(request, track_id):
    if not request.user.is_authenticated:
        return redirect('/login')

    track = Track.objects.get(id=track_id)
    request.user.favorite_tracks.add(track)
    return redirect('/favorites')

def remove_from_favorites(request, track_id):
    if not request.user.is_authenticated:
        return redirect('/login')

    track = Track.objects.get(id=track_id)
    request.user.favorite_tracks.remove(track)
    return redirect('/favorites')

def favorites(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    favorite_tracks = request.user.favorite_tracks.all()
    return render(request, 'favorites.html', {'favorite_tracks': favorite_tracks})