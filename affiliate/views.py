from django.shortcuts import render,redirect,get_object_or_404
from .form import AffiliateForm,LoginForm,ProductSearchForm
from .models import Affiliate
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    affiliates = Affiliate.objects.all().order_by('-id')  # Fetch all records
    paginator = Paginator(affiliates, 5)  # Show 5 items per page

    page_number = request.GET.get('page')  # Get the page number from URL
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'affiliate/home.html', {'page_obj': page_obj})

# search product
def search_products(request):
    query = request.GET.get('query', '')
    products = Affiliate.objects.filter(title__icontains=query)if query else ''
    
    form = ProductSearchForm(request.GET)
    
    return render(request, 'affiliate/search.html', {'form': form, 'products': products})

# def search_view(request):
#     query = request.GET.get('q', '')  # Get search query from URL
#     products = Affiliate.objects.filter(name__icontains=query) if query else []
#     return render(request, 'affiliate/search.html', {'products': products, 'query': query})


# admin login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add/')  # Redirect to a success page
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'affiliate/login.html', {'form': form})

def out(request):
    logout(request)
    return redirect('login')

# admin panel
@login_required(login_url='login')
def admin(request):
    affiliates = Affiliate.objects.all().order_by('-id').values() 
   
    return render(request, 'affiliate/admin.html', {'affiliates': affiliates})



@login_required(login_url='login')
def add(request):
    if request.method == 'POST':        
        form = AffiliateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            
            if Affiliate.objects.filter(title=title).exists():
                messages.error(request, "Product already exists with this title")
                return redirect(request.path)
            
            form.save()
            messages.success(request, "Product Added.")
 # Change 'success' to your success page URL
    else:
        form = AffiliateForm()

    return render(request, 'affiliate/add_affiliate.html', {'form': form})


# update
@login_required(login_url='login')
def update_affiliate(request, id):  # Ensure 'id' is passed here
    affiliate = get_object_or_404(Affiliate, id=id)
    
    if request.method == "POST":
        form = AffiliateForm(request.POST, instance=affiliate)
        if form.is_valid():
            form.save()
            return redirect('admin')  # Redirect after updating
    
    else:
        form = AffiliateForm(instance=affiliate)

    return render(request, 'affiliate/update.html', {'form': form})

@login_required(login_url='login')
def delete_affiliate(request, id):
    affiliate = get_object_or_404(Affiliate, id=id)
    affiliate.delete()
    return redirect('admin') 


def base(request):
    return render(request,'affiliate/base.html')