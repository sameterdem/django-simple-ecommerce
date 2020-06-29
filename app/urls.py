from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from product.views import category
from pages.views import search, search_autocomplete

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('user.urls')),
    path('search/', search, name="search"),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('category/<slug:cat_slug>', category, name="category"),
    url('search_autocomplete/', search_autocomplete, name='search_autocomplete'),
    url(r'^admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
