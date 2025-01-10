from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def resources(request) :
    return render(request, 'resources.html')

def duplication(request) :
    return render(request, 'duplication.html')