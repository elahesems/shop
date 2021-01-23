from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from web.models import *
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .widgets import navbarVariables
import random
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

@unauthenticated_user
def loginPage(request):
    print('this is login page')
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':#ghguyı
            print('etelaat gerefte shod')
            username = request.POST.get('username_user')
            password = request.POST.get('password_user')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')


        return render(request, 'login.html')


@unauthenticated_user #hanuz login nashode sabtenam nashode_
def registerPage(request):
    if request.user.is_authenticated:#{age fard login shode_
        return redirect('home')#_befrestesh be 'home'page.
    else:#ama age login nashode:
        form = CreateUserForm #inja chon requestemun "get" hastesh in formo avval migre (1)
        if request.method == 'POST': #request "post" miyad inja (3)
            form = CreateUserForm(request.POST) #ettelaato control mikene (4)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html',context) # bad az inke formo gereft  va ettelaato ke minevisim bad az click renderesh mikone(2)


def logoutUser(request):
    logout(request)
    return redirect('login')



def home(request):

    sliders=Sliders.objects.all()
    products = Product.objects.all()
    randlist = random.choices(products, k=3)

    theUrl = request.path
    if theUrl == '/':
        isHomePage = True

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

    context = {'isHomePage':isHomePage,'sliders':sliders,
               'products':products,'kadinList':kadinList,'erkekList':erkekList,
               'aksesuarList':aksesuarList,'footer':footer,'randlist':randlist}

    navbarVariables(context=context)

    return render(request,'index.html',context)



@login_required(login_url='login')

def shop_detail(request,productSpeciality='',category=''):
    allProducts=Product.objects.filter(productSpeciality=productSpeciality)
    products=[]
    for product in allProducts:
        if category in product.category:
            products.append(product)

    context = {'products': products}
    navbarVariables(context=context)


    return render(request, 'shop.html', context)




@login_required(login_url='login')
def shop(request):
    products = Product.objects.all().order_by('-id')

    context = {'products':products}
    navbarVariables(context=context)
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def seyirci(request):
    seyirci = Seyirci.objects.all()
    brands = Brands.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        emailOfCustomer = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        dateOfMail = datetime.now()
        formatDate = dateOfMail.strftime("%Y-%M-%d %H:%M:%S")
        text = f"Yeni başvuru bilgileri adı: {name}                       tarih:{formatDate} \n " \
               f"eposta adresi: {emailOfCustomer} \r bu konoda: {subject} \r\n\n" \
               f" bu mesajı göndermiştir: {message}"
        textOfCustomer = f'Sayın{name} mesajınız bize başarıyla gönderildi'
        title = 'Yeni Başvuru Var!'
        titleOfCustomer = 'mesajınız bize ulaşmıştır!'

        hostEmail = settings.EMAIL_HOST_USER
        sent_to = [hostEmail]

        sendToCustomer = [emailOfCustomer]
        print(sendToCustomer)
        print(hostEmail)

        try:
            send_mail(title, text, hostEmail, sent_to, fail_silently=False)
            send_mail(titleOfCustomer, textOfCustomer, hostEmail, sendToCustomer, fail_silently=False)
            messages.info(request, 'Mesajiniz başarılı bir şekilde gönderildi!')
        except:
            message.error(request, 'Bir hata uluştu lütfen tekrar deneyiniz!')

    context ={'seyirci':seyirci,'brands':brands}
    navbarVariables(context=context)
    return render(request, 'contact.html', context)


def team_member(request):
    memberById = Team_member.objects.all()
    brands = Brands.objects.all()

    context = {'memberById':memberById,'brands':brands}
    navbarVariables(context=context)
    return render(request, 'about.html', context)

def product_details(request,pk):
    print('ok')
    product = Product.objects.get(id=pk)
    context = {'product':product}
    navbarVariables(context=context)
    return render(request, 'product-details.html', context)
