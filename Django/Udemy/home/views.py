from django.shortcuts import render

context = {'texto': 'Olá Mundo!'}

# Create your views here.
def home(request):
    return render(request, 'home/home.html', context)