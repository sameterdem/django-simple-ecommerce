from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('product/', include('product.urls')),
    url(r'^admin/', admin.site.urls)
]
