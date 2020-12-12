from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from web.models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html',context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    sliders=Sliders.objects.all()
    products = Product.objects.all()
    theUrl = request.path
    if theUrl == '/':
        isHomePage = True

    categoriesList = Product._meta.get_field('category').choices
    categories=[]
    for i in categoriesList:
        categories.append(i[0])

    productsByDate=Product.objects.all().order_by('-inDate')

    productsByid=productsByDate.order_by('-id')

    kadinList=[]
    i=0
    for product in productsByid:

        if 'kadin' in product.category:

            kadinList.append(product)
            i += 1
            if i==8:
                break

    erkekList = []
    i = 0
    for product in productsByid:

        if 'erkek' in product.category:

            erkekList.append(product)
            i += 1
            if i == 8:
                break

    aksesuarList = []
    i = 0
    for product in productsByid:

        if 'aksesuar' in product.category:

            aksesuarList.append(product)
            i += 1
            if i == 8:
                break

    footer = Footer.objects.all()

    context = {'isHomePage':isHomePage,'sliders':sliders,'products':products,'categories':categories,'kadinList':kadinList,'erkekList':erkekList,'aksesuarList':aksesuarList,'footer':footer}
    return render(request,'index.html',context)

@login_required(login_url='login')
def shop(request):
    products = Product.objects.all().order_by('-id')
    categoriesList = Product._meta.get_field('category').choices
    categories=[]
    for i in categoriesList:
        categories.append(i[0])

    productsByDate = Product.objects.all().order_by('-inDate')

    productsByid = productsByDate.order_by('-id')

    kadinList=[]
    i=0
    for product in productsByid:

        if 'kadin' in product.category:

            kadinList.append(product)
            i += 1
            if i==8:
                break

    erkekList = []
    i = 0
    for product in productsByid:

        if 'erkek' in product.category:

            erkekList.append(product)
            i += 1
            if i == 8:
                break

    aksesuarList = []
    i = 0
    for product in productsByid:

        if 'aksesuar' in product.category:

            aksesuarList.append(product)
            i += 1
            if i == 8:
                break



    context = {'products': products,'kadinList': kadinList,'erkekList': erkekList,'aksesuarList':aksesuarList,'categories':categories}
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def seyirci(request):
    seyirci = Seyirci.objects.all()
    brands = Brands.objects.all()

    context ={'seyirci':seyirci,'brands':brands}
    return render(request, 'contact.html', context)


def about(request):
    about = AboutUs.objects.all()
    brands = Brands.objects.all()
    context = {'about':about, 'brands':brands}
    return render(request, 'about.html', context)



