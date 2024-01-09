from watchlist.views import WatchListDetailView, WatchListView
from django.urls import path, include

urlpatterns = [
    path('list/', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailView.as_view(), name='movie-details'),
]
