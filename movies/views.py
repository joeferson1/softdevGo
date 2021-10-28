from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from movies.models import Movie
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render (request, 'movies/list.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        date_release = request.POST['date_release']
       
        Movie.objects.create(title=title, date_release=date_release)
        return HttpResponseRedirect (reverse('movies_list'))
        
    else:
        return render(request, 'movies/create.html')
def update(request, movie_id):
    movie  = get_object_or_404(Movie, id=movie_id)

    if request.method =='POST':
        title = request.POST ['title']
        date_release  = request.POST['date_release']

        movie.title = title
        movie.date_release = date_release
        movie.save()
        return HttpResponseRedirect(reverse('movie_detail', kwargs={'movie_id': movie_id}))
    else:
        d = movie.date_release
        date_release = f'{d.year}-{d.month:02d}-{d.day}'

        context = {
            'movie': movie,
            'date_release': date_release
        }
        return render(request, 'movies/update.html', context)

