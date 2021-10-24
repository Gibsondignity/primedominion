from django.http import request, response, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

import accountant
from .models import *
from .forms import AddContractForm


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.

def accountantLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	return render(request, 'accountant/accountantLogin.html')




@login_required(login_url='accountantLogin')
def accountantLogout(request):
	logout(request)
	return redirect('accountantLogin')




@login_required(login_url='accountantLogin')
def home(request):
    if 'data' in request.GET:
        data = request.GET['data']
        supplier_queryset  = Supplier.objects.filter(name__icontains=data)
    else:
        supplier_queryset = Supplier.objects.all()

    contracts = Contract.objects.all()
    total_suppliers = Supplier.objects.all().count()
    total_contracts = Contract.objects.all().count()

    transactions = Accountant.objects.all()
    total_transactions = Accountant.objects.all().count()
	
    
    context = {'supplier_queryset':supplier_queryset, "contracts":contracts, "total_suppliers":total_suppliers, "total_contracts":total_contracts, "transactions":transactions, "total_transactions":total_transactions }
    
    return render(request, 'accountant/home.html', context)





@login_required(login_url='accountantLogin')
def transaction(request):
	form = AddContractForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			transaction = form.save(commit=False)
			transaction.save()
			messages.success(request, 'New Transaction has been added successfuly')
			#return redirect('home')
		else:
			messages.error(request, 'Failed to add new Transaction')

	context = {"form":form}
      
	return render(request, 'accountant/transaction.html', context)





@login_required(login_url='accountantLogin')
def records(request):

    return render(request, 'accountant/records.html')





@login_required(login_url='accountantLogin')
def update_payment(request, pk):

	update_s = Accountant.objects.get(pk=pk)
	form = AddContractForm(instance=update_s)

	if request.method == 'POST':
		form = AddContractForm(request.POST, instance=update_s)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {"form":form, "update_s":update_s}
	return render(request, 'accountant/update_payment.html', context)



@login_required(login_url='accountantLogin')
def transact_for_supplier(request, pk):

	supplier = get_object_or_404(Supplier, pk=pk)
	contract_invoice = supplier.contract_set.all()
	
	form = AddContractForm(instance=supplier)

	context = {'supplier':supplier, 'form':form, 'contract_invoice':contract_invoice}
	return render(request, 'accountant/transact_for_supplier.html', context)






@login_required(login_url='accountantLogin')
def supplier_details(request, pk):
	view_details = get_object_or_404(Supplier, pk=pk)
	contracts = view_details.contract_set.all()

	context = {"supplier":view_details, "contracts":contracts}
	return render(request, 'accountant/supplier_account_details.html', context)







@login_required(login_url='accountantLogin')
def delete_transaction(request, pk):

	del_transaction = Accountant.objects.get(pk=pk)
	if request.method == "POST":
		del_transaction.delete()
		return redirect('home')

	context = {'del_transaction':del_transaction}
	return render(request, 'accountant/delete_transaction.html', context)



@login_required(login_url='accountantLogin')
def contract_details(request):

    suppliers = Supplier.objects.all()
    total_suppliers = Supplier.objects.all().count()
    return render(request, 'app/list_suppliers.html', {"suppliers": suppliers, "total_suppliers":total_suppliers})


@login_required(login_url='accountantLogin')
def contract_details(request):

    suppliers = Supplier.objects.all()
    total_suppliers = Supplier.objects.all().count()
    return render(request, 'app/list_suppliers.html', {"suppliers": suppliers, "total_suppliers":total_suppliers})




'''
@login_required(login_url='login')
def list_suppliers(request):

    suppliers = Supplier.objects.all()
    total_suppliers = Supplier.objects.all().count()
    return render(request, 'app/list_suppliers.html', {"suppliers": suppliers, "total_suppliers":total_suppliers})




def view_record(request, pk):
	view_details = get_object_or_404(Supplier, pk=pk)
	#supplier_contracts = Contract.objects.select_related('supplier').get(pk=pk)
	return render(request, 'app/supplier_details.html', {"supplier":view_details})



@login_required(login_url='login')
def contract_list(request):

    contracts = Contract.objects.all()
    total_contracts = Contract.objects.all().count()
    return render(request, 'app/contract_list.html', {"contracts":contracts, "total_contracts":total_contracts})
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




