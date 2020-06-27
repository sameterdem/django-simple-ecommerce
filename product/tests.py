from django.test import TestCase
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
