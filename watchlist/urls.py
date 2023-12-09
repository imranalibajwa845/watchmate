from watchlist.views import MovieDetailView, MovieListView
from django.urls import path, include

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-details'),
]
