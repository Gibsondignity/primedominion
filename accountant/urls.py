from django.urls import path
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

from . import views
 
urlpatterns = [
    
    path('accountant/accountantLogin/', views.accountantLogin, name="accountantLogin"),
    path('accountant/home/', views.home, name="home"),
    path('accountant/transaction/', views.transaction, name='transaction'),
    path('accountant/records/', views.records, name='records'),
    # path('contract_continues/', views.contract_continues, name='contract_continues'),
    path('accountant/suppliers_data_list/', views.suppliers_data_list, name='suppliers_data_list'),
    
    path('accountant/home/supplier_details/<int:pk>/', views.supplier_details, name="supplier_details"),
    path('accountant/home/update/<int:pk>/', views.update_payment, name='update_payment'),
    # path('index/update/<int:pk>/', views.update_supplier, name='update_supplier'),
    path('accountant/home/delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    
    path('accountant/records/list_all_contracts', views.list_all_contracts, name='list_all_contracts'),
    path('accountant/records/list_transactions', views.list_transactions, name='list_transactions'),
    # path('transactions', views.transactions, name='transactions'),
    path('accountant/accountantLogout', views.accountantLogout, name='accountantLogout'),
    
    path('accountant/home/transact_for_supplier/<int:pk>/', views.transact_for_supplier, name='transact_for_supplier'),
    #  path('index/update_contract/<int:pk>/', views.update_contract, name='update_contract'),


    path("password_reset", views.password_reset_request, name="password_reset")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


