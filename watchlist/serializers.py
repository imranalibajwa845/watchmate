from rest_framework import serializers
from watchlist.models import Movie

def name_length(value):
    if len(value) < 3:
        raise serializers.ValidationError("Name is too short")

class MovieSerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name  = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name, validators=[name_length])
        instance.description = validated_data.get(
                                        'description',  instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance

    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Name and description should be different!")

        return data
