from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:track_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:track_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
