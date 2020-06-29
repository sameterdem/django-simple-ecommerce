import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

from product.models import Category, Product
from pages.forms import SearchForm

def index(request):
    context = dict()
    context['items'] = Product.objects.filter(
        status = 'True',
    )
    return render(request, 'index.html', context)

def search(request):
    if request.method == 'POST': 
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] 
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search.html', context)

    return HttpResponseRedirect('/')

def search_autocomplete(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for item in products:
      product_json = {}
      product_json = item.title
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
