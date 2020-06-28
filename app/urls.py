from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from product.views import category

urlpatterns = [
    path('', include('pages.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('category/<slug:cat_slug>', category, name="category"),
    url(r'^admin/', admin.site.urls)
]
