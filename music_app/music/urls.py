from django.urls import path
from . import views

urlpatterns = [
    # Маршруты для поиска и избранного
    path('search/', views.search, name='search'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:track_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:track_id>/', views.remove_from_favorites, name='remove_from_favorites'),

    # Маршруты для радио
    path('radio/', views.radio_list, name='radio_list'),  # Список радиостанций
    path('radio/<int:pk>/', views.radio_detail, name='radio_detail'),  # Детальный просмотр радиостанции
]