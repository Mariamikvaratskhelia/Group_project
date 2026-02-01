from django.urls import path
from .views import index, movies_list_create, reviews_list_create, movie_delete, movie_reviews

urlpatterns = [
    path("", index),                  # 👈 THIS maps /api/ to index.html
    path("movies/", movies_list_create),
    path("movies/<int:id>/", movie_delete),
    path("movies/<int:movie_id>/reviews/", movie_reviews),
    path("reviews/", reviews_list_create),
]
