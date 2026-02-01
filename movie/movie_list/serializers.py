from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("id", "created_at")
