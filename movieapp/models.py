from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    time_length = models.CharField(max_length=100)
    rating_critics = models.CharField(max_length=100)
    rating_audience = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)


    def __str__(self):
        return self.name + ' | ' + self.genre + '  | ' + self.time_length + ' | ' + self.rating_critics + ' | ' + self.rating_audience + ' | ' + self.platform







