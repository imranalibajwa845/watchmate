from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=250)
    about = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
