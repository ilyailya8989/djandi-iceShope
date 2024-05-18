from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def index1(request):
    return render(request, 'posts/index1.html')

def contact(request):
    return render(request, 'posts/contakt.html')