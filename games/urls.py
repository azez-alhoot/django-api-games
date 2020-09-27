from django.urls import path

from .views import GameList, GameDetails

urlpatterns = [
    path('',GameList.as_view(), name='games'),
    path('<int:pk>/',GameDetails.as_view(), name='games_details'),
]