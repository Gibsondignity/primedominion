from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('', views.loginPage, name="login"),
    path('index/', views.index, name="index"),
    path('new_supplier/', views.new_supplier, name='new_supplier'),
    path('contract_continues/', views.contract_continues, name='contract_continues'),
    path('records/', views.records, name='records'),
    path('records/list_suppliers/', views.list_suppliers, name='list_suppliers'),
    
    path('index/view_record/<int:pk>/', views.view_record, name="view_record"),
    path('update_supplier/<int:pk>', views.update_supplier, name='update_supplier'),
    path('index/update/<int:pk>/', views.update_supplier, name='update_supplier'),
    path('delete_supplier/<int:pk>/', views.delete_supplier, name='delete_supplier'),
    
    path('records/contract_list', views.contract_list, name='contract_list'),
    #path('transactions', views.transactions, name='transactions'),
    path('logoutUser', views.logoutUser, name='logout'),
    
    
    path("password_reset", views.password_reset_request, name="password_reset")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


