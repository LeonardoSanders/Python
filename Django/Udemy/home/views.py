from django.shortcuts import render
from home.data import posts


# Create your views here.
def home(request):
    context = {
        'texto': 'Olá Mundo!',
        'posts': posts
        }
    return render(request, 'home/home.html', context)