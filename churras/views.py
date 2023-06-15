from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    pratos = {
        1: 'Picanha',
        2: 'Fraldinha',
        3: 'Maminha'
    }
    
    contexto = {
        'lista_pratos' : pratos,
        
    }
    return render(request, 'index.html', contexto)
    # return HttpResponse('<h1>Churrasco-canes</h1')

