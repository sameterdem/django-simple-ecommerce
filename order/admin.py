from django.contrib import admin

from order.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display    = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter     = ['user']

    

admin.site.register(Cart, CartAdmin)