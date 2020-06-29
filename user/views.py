from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout, update_session_auth_hash

from user.forms import SignUpForm, UserProfile, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile
from order.models import Order, OrderProduct

@login_required(login_url='/login')
def account(request):
    context = dict()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context['profile'] = profile
    return render(request, 'account.html', context)

@login_required(login_url='/login')
def orders(request):
    context = dict()
    current_user = request.user
    orders=Order.objects.filter(user_id=current_user.id)
    context['orders'] = orders
    return render(request, 'order_history.html', context)

@login_required(login_url='/login')
def order_detail(request, id):
    context = dict()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context['order'] = order
    context['orderitems'] = orderitems
    return render(request, 'order_detail.html', context)

@login_required(login_url='/login')
def account_edit(request):
    context = dict()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Bilgiler güncellendi.')
            return HttpResponseRedirect('/account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context['user_form'] = user_form
        context['profile_form'] = profile_form

    return render(request, 'account_edit.html', context)

@login_required(login_url='/login')
def change_password(request):
    context = dict()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre değiştirildi.')
            return HttpResponseRedirect('/account')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect('/account/password')
    else:
        form = PasswordChangeForm(request.user)
        context['form'] = form
    return render(request, 'change_password.html', context)


def signup(request):
    context = dict()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Kayıt işlemi başarılı.')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
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
            messages.error(request, "Kullanıcı adı veya şifreniz yanliş.")
            return HttpResponseRedirect('/login')


    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')