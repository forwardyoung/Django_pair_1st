from django.shortcuts import render
from .models import Review


# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def new(request):
    return render(request, 'movie/new')