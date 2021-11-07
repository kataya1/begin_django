from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import MovieForm
from .models import Movie

# we will get this from the database 
movie_list = []
# Create your views here.
def index(request):
    # return HttpResponse('hello fuckface')
    return render(request, 'movies/index.html', context={ 'movie_list': Movie.objects.all()} )

def add_movie(request):
    if request.method == 'GET':
        return render(request, 'movies/movie_add.html', context={ 'form': MovieForm() })
    elif request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            m = Movie(name=name)
            m.save()
            return redirect('movies:index')
        else:
            return render(request, 'movies/movie_add.html', context={ 'form': form })

