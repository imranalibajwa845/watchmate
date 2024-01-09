from rest_framework import serializers
from watchlist.models import WatchList


class WatchListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'
