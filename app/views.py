from django.http import request, response, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product, Transaction
from .forms import AddSupplierForm, AddProductForm, TransactionForm, PasswordResetForm

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Create your views here.
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'app/login.html', context)



@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def index(request):
    product_queryset = Product.objects.all()
    if request.method == "POST":
        category = request.POST.get('dropdown')
        search_data = request.POST.get('search_data')

        if category == "Supplier":
            if search_data != "":
                supplier_queryset = Supplier.objects.filter(name__contains=search_data)
                return render(request, 'app/index.html', {"supplier_queryset":supplier_queryset, "product_queryset":product_queryset})
            else:
                return HttpResponse('<p>Enter either supplier name or product name to search</p>')
    
        elif category == "Products":
            return HttpResponse('<p> We have not implemented other saerch yet. Search for only supplier and track the other relationships </p>')

        else:
            return HttpResponse('<p> We have not implemented other saerch yet. Search for only supplier and track the other relationships </p>')


    else:
        supplier_queryset = Supplier.objects.all()
        product_queryset = Product.objects.all()
        return render(request, 'app/index.html', {"supplier_queryset":supplier_queryset, "product_queryset":product_queryset})




@login_required(login_url='login')
def new_supplier(request):

    form = AddSupplierForm()

    if request.method == "POST":
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            messages.success(request, "New Supplier Added Successfully")
            return redirect("records")
        else:
            messages.error(request, "Failed to add new supplier")
            
    
    return render(request, 'app/add_supplier.html', {"form": form})



@login_required(login_url='login')
def new_product(request):
    
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        form = AddProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "New Supplier Added Successfully")
            return redirect('records')
        else:
            messages.error(request, "Failed to Add New Produce")

    else:
        return render(request, 'app/add_product.html', {"suppliers":suppliers})

    
    return render(request, 'app/add_product.html', {"form": form, "suppliers":suppliers})
 


@login_required(login_url='login')
def records(request):

    return render(request, 'app/records.html')



@login_required(login_url='login')
def list_suppliers(request):

    suppliers = Supplier.objects.all()
    total_suppliers = Supplier.objects.all().count()
    return render(request, 'app/list_suppliers.html', {"suppliers": suppliers, "total_suppliers":total_suppliers})



@login_required(login_url='login')
def list_products(request):
    
    products = Product.objects.all()

    totat_producct = Product.objects.all().count()
    
    return render(request, 'app/list_products.html', {"products": products, "totat_producct":totat_producct})



@login_required(login_url='login')
def transactions(request):

    form = TransactionForm()

    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            messages.success(request, "New Transaction Added Successfully")
            return redirect("records")
        else:
            messages.error(request, "Failed to add new transaction")
            
    suppliers = Supplier.objects.all()
    
    return render(request, 'app/transaction.html', {"form": form, "suppliers": suppliers})



@login_required(login_url='login')
def list_transactions(request):

    transactions = Transaction.objects.all()
    total_transactions = Transaction.objects.all().count()
    return render(request, 'app/list_transaction.html', {"transactions":transactions, "total_transactions":total_transactions})


'''
Password reset form using in-built django form 
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
'''


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})








