from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View
# Create your views here.

class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug, draft=False)
        return render(request, "movies/movie_detail.html", {"movie": movie})
