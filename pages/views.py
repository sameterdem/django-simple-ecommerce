from django.shortcuts import render
from product.models import Category

def index(request):
    context = dict()
    return render(request, 'index.html', context)