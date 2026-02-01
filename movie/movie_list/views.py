from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


# ✅ MOVIES: GET + POST
@api_view(["GET", "POST"])
def movies_list_create(request):
    if request.method == "GET":
        movies = Movie.objects.all().order_by("-created_at")
        serializer = MovieSerializer(movies, many=True)
        return Response({"movies": serializer.data}, status=status.HTTP_200_OK)

    # POST
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        movie = serializer.save()
        return Response(
            {"new_movie": MovieSerializer(movie).data},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ⭐ BONUS: DELETE movie
@api_view(["DELETE"])
def movie_delete(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    movie.delete()
    return Response({"message": "Movie deleted successfully"}, status=status.HTTP_200_OK)


# ✅ REVIEWS: GET + POST (separate endpoint)
@api_view(["GET", "POST"])
def reviews_list_create(request):
    if request.method == "GET":
        reviews = Review.objects.all().order_by("-created_at")
        serializer = ReviewSerializer(reviews, many=True)
        return Response({"reviews": serializer.data}, status=status.HTTP_200_OK)

    # POST
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = serializer.save()
        return Response(
            {"new_review": ReviewSerializer(review).data},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def movie_reviews(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id).order_by("-created_at")
    serializer = ReviewSerializer(reviews, many=True)
    return Response({"reviews": serializer.data}, status=status.HTTP_200_OK)



from django.shortcuts import render

def index(request):
    movies = Movie.objects.all()
    return render(request, "movie_list/index.html", {"movies": movies})
