from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request, slug):
    context = dict()
    return render(request, 'products.html', context)

def category(request, cat_slug):
    context = dict()

    # Get categories by category sub
    context['category'] = get_object_or_404(Category, slug=cat_slug)
    context['items'] = Product.objects.filter(
        category = context['category'],
        status = 'True',
    )
    
    return render(request, 'category.html', context)
