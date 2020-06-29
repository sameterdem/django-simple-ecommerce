from order.models import Cart
from product.models import Category

def basket_data(request):
    context             = dict()
    category            = Category.objects.all()
    current_user        = request.user
    cart                = Cart.objects.filter(user_id=current_user.id)
    total               = 0
    count               = 0
    for item in cart:
        total    += item.product.price * item.quantity
        count    += item.quantity
        context['basket_total']     = total
        context['basket_products']  = cart
        context['basket_count']     = count
    return context