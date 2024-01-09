from rest_framework import serializers
from watchlist.models import StreamPlatform, WatchList


class WatchListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerilizer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'
