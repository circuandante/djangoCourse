from django.shortcuts import render
# Create your views here.


def proof(request):
    name = 'andres'
    return render(request, 'index.html', {'names': name})
