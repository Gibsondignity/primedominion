from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('PA/PALogin', views.loginPage, name="login"),
    path('PA/index/', views.index, name="index"),
    path('PA/new_supplier/', views.new_supplier, name='new_supplier'),
    path('PA/contract_continues/', views.contract_continues, name='contract_continues'),
    path('PA/records/', views.records, name='records'),
    path('PA/records/list_suppliers/', views.list_suppliers, name='list_suppliers'),
    
    path('PA/index/view_record/<int:pk>/', views.view_record, name="view_record"),
    path('PA/update_supplier/<int:pk>', views.update_supplier, name='update_supplier'),
    path('PA/index/update/<int:pk>/', views.update_supplier, name='update_supplier'),
    path('PA/delete_supplier/<int:pk>/', views.delete_supplier, name='delete_supplier'),
    
    path('PA/records/contract_list', views.contract_list, name='contract_list'),
    #path('transactions', views.transactions, name='transactions'),
    path('PA/logoutUser', views.logoutUser, name='logout'),
    
     path('PA/index/delete_contract/<int:pk>/', views.delete_contract, name='delete_contract'),
     path('PA/index/update_contract/<int:pk>/', views.update_contract, name='update_contract'),


    path("password_reset", views.password_reset_request, name="password_reset")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


