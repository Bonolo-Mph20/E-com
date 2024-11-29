from django.shortcuts import render
from .models import Shoes

# Create your views here.

#from django.shortcuts import render
from django.http import HttpResponse

def store(request):

    shoes = Shoes.objects.all()

    return render(request, 'index.html', {'shoes': shoes})