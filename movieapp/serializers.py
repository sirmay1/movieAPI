from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'genre', 'time_length', 'rating_critics', 'rating_audience', 'platform')
