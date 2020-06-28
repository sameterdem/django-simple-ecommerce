from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from product.models import Category, Product
from .models import Cart, CartForm, Order, OrderForm, OrderProduct

def index(request):
    context = dict()
    category = Category.objects.all()
    current_user = request.user
    cart = Cart.objects.filter(user_id=current_user.id)
    total=0
    for item in cart:
        total += item.product.price * item.quantity
        context['total']    = total
        context['cart']     = cart
    return render(request, 'cart.html', context)

@login_required(login_url='/login')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER') 
    current_user = request.user 

    checkproduct = Cart.objects.filter(product_id=id) 
    if checkproduct:
        control = 1
    else:
        control = 0 

    if request.method == 'POST':  
        form = CartForm(request.POST)
        if form.is_valid():
           if control==1: 
                data = Cart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save() 
           else :
                data = Cart()
                data.user_id = current_user.id
                data.product_id =id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Sepete Eklendi ")
        return HttpResponseRedirect(url)

    else: 
        if control == 1: 
            data = Cart.objects.get(product_id=id)
            data.quantity += 1
            data.save()  
        else:  
            data = Cart()  
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  
        messages.success(request, "Sepete Eklendi")
        return HttpResponseRedirect(url)

@login_required(login_url='/login')
def deletefromcart(request, id):
    Cart.objects.filter(id=id).delete()
    messages.success(request, "Urun silindi.")
    return HttpResponseRedirect("/order")

@login_required(login_url='/login')
def checkout(request):
    context      = dict()

    category     = Category.objects.all()
    current_user = request.user
    cart         = Cart.objects.filter(user_id=current_user.id)
    total        = 0
    for rs in cart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data            = Order()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name  = form.cleaned_data['last_name']
            data.address    = form.cleaned_data['address']
            data.city       = form.cleaned_data['city']
            data.phone      = form.cleaned_data['phone']
            data.user_id    = current_user.id
            data.total      = total
            data.ip         = request.META.get('REMOTE_ADDR')
            ordercode       = get_random_string(5).upper()
            data.code       =  ordercode
            data.save() 

            cart = Cart.objects.filter(user_id=current_user.id)
            for item in cart:
                detail = OrderProduct()
                detail.order_id     = data.id # Order Id
                detail.product_id   = item.product_id
                detail.user_id      = current_user.id
                detail.quantity     = item.quantity
                detail.price        = item.product.price
                detail.amount       = item.amount
                detail.save()
                
                product = Product.objects.get(id=item.product_id)
                product.amount -= item.quantity
                product.save()

            Cart.objects.filter(user_id=current_user.id).delete() 
            request.session['cart_items']=0
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'checkoutInfo.html',{'ordercode':ordercode,'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/checkout")

    form    = OrderForm()
    cart    = Cart.objects.filter(user_id=current_user.id)
    context['cart'] = cart
    context['category'] = category
    context['total'] = total
    context['form'] = form
    return render(request, 'checkout.html', context)