from django.shortcuts import render
from watchlist.models import Movie
from django.http import JsonResponse
from watchlist.serializers import MovieSerilizer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerilizer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = MovieSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerilizer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerilizer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerilizer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(id=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
