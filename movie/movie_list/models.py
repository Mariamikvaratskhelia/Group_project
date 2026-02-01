from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    rating = models.PositiveSmallIntegerField()      # 0..10 validated in serializer
    duration_minutes = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    actors = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()      # 0..10 validated in serializer
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.name}"
