from django.shortcuts import render

# Create your views here.

def homepage(request): #request sãorequisicoes do site, podem ser de get ou post

    return render (request, 'homepage.html')