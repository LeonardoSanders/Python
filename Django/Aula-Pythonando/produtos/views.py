from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_produto(request):
    return render(request, 'ver_produto.html', {'nome': 'Léo'})

def inserir_produto(request):
    return HttpResponse('Estou no inserir')