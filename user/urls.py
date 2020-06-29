from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('account/', views.account, name="account"),
    path('account/orders', views.orders, name="orders"),
    path('account/orders/detail/<int:id>', views.order_detail, name="order_detail"),
    path('account/edit', views.account_edit, name="account_edit"),
    path('account/password', views.change_password, name="change_password"),
]
