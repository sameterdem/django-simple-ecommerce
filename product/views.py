from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Images

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

def detail(request, id, slug):
    context = dict()
    #Get product 
    context['product'] = Product.objects.filter(
        id = id
    )

    #Get product all images
    context['images'] = Images.objects.filter(
        products_id = id
    )
    return render(request, 'product_detail.html', context)
