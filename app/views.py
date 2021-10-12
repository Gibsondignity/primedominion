from django.http import request, response, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product
from .forms import AddSupplierForm, AddProductForm



# Create your views here.
def index(request):
    supplier_queryset = Supplier.objects.all()
    product_queryset = Product.objects.all()
    if request.method == "POST":
        category = request.POST.get('dropdown')
        search_data = request.POST.get('search_data')
        print(category)
        print(search_data)

        if category == "Supplier":
            if search_data != "":
                queryset = supplier_queryset.filter(name__contains=search_data)
            else:
                return HttpResponse('<p>Enter either supplier name or product name to search</p>')
    
            return render(request, 'app/index.html', {"queryset": queryset, "category": category})

        if category == "Products":
            if search_data != "":
                queryset = product_queryset.filter(name__contains=search_data)
            else:
                return HttpResponse('<p>Enter either supplier name or product name to search</p>')
    
            return render(request, 'app/index.html', {"queryset": queryset, "category": category})

    else:
        return render(request, 'app/index.html')





def new_supplier(request):

    form = AddSupplierForm()

    if request.method == "POST":
        form = AddSupplierForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            messages.success(request, "New Supplier Added Successfully")
            return redirect("new_supplier")
        else:
            messages.error(request, "Failed to add new supplier")
            return redirect('index')
    
    return render(request, 'app/add_supplier.html', {"form": form})


def new_product(request):
    all_suppiers = Supplier.objects.all()
    print(all_suppiers)
    form = AddProductForm(request.POST or None)

    if request.method == "POST":

        form = AddProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "New Supplier Added Successfully")
            return redirect('index')
        else:
            messages.error(request, "Failed to Add Supplier")

    else:
        return render(request, 'app/add_product.html')

    return render(request, 'app/add_product.html', {"form": form, "all_suppiers":all_suppiers})
 



def records(request):

    return render(request, 'app/records.html')



def list_suppliers(request):

    suppliers = Supplier.objects.all()

    return render(request, 'app/list_suppliers.html', {"suppliers": suppliers})


def list_products(request):
    
    products = Product.objects.all()
    for product in products:
        total_invoice = (product.invoice_amount * product.quantity)

    return render(request, 'app/list_products.html', {"products": products, "total_invoice": total_invoice})


def list_transactions(request):

    return render(request, 'app/list_transaction.html')











