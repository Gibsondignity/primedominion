from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    
    path('', views.loginPage, name="login"),
    path('index/', views.index, name="index"),
    path('new_supplier/', views.new_supplier, name='new_supplier'),
    path('new_product/', views.new_product, name='new_product'),
    path('records/', views.records, name='records'),
    path('records/list_suppliers', views.list_suppliers, name='list_suppliers'),
    path('records/list_products', views.list_products, name='list_products'),
    path('records/list_transactions', views.list_transactions, name='list_transactions'),
    path('transactions', views.transactions, name='transactions'),
    path('logoutUser', views.logoutUser, name='logout'),
    
    
    path("password_reset", views.password_reset_request, name="password_reset")
]
