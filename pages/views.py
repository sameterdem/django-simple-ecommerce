from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

from product.models import Category
from pages.forms import SignUpForm

def index(request):
    context = dict()
    return render(request, 'index.html', context)

def signup(request):
    context = dict()
     # User already logged in
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    # Sign Up
    form = SignUpForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # User auto login
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, 'signup.html', context)


def login(request):
    context = dict()

    # User already logged in
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    # Login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Kullanici adi ya da sifre yanlis.')
            return HttpResponseRedirect('/login')


    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
