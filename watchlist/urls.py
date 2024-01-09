from watchlist.views import (
    StreamView,
    StreamDetailView,
    WatchListView,
    WatchListDetailView,
)
from django.urls import path, include

urlpatterns = [
    path('watchlist/', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailView.as_view(), name='movie-details'),
    path('streams/', StreamView.as_view(), name='stream-list'),
    path('<int:pk>', StreamDetailView.as_view(), name='stream-details'),
]
