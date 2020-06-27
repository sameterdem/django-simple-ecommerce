from django.shortcuts import render
from product.models import Category

def index(request):
    context = dict()
    
    # Get all categories
    context['categories'] = Category.objects.filter(
       status = 'True',
    ).order_by('title')

    return render(request, 'index.html', context)