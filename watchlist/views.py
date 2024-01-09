from django.shortcuts import render
from watchlist.models import WatchList
from django.http import JsonResponse
from watchlist.serializers import WatchListSerilizer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class WatchListView(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerilizer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = WatchListSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailView(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerilizer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
            WatchList.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = WatchList.objects.all()
        serializer = WatchListSerilizer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WatchListSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerilizer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        try:
            movie = WatchList.objects.get(id=pk)
            WatchList.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
