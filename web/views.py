from django.shortcuts import render, redirect


# Create your views here.
from web.models import *


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


def shop(request):
    products = Product.objects.all().order_by('-id')
    # categoriesList = Product._meta.get_field('category').choices
    # categories = []
    # for i in categoriesList:
    #     categories.append(i[0])
    #
    # kadinList = []
    # i = 0
    # for product in products:
    #
    #     if 'kadin' in product.category:
    #
    #         kadinList.append(product)
    #         i += 1
    #
    #
    # erkekList = []
    # i = 0
    # for product in products:
    #
    #     if 'erkek' in product.category:
    #
    #         erkekList.append(product)
    #         i += 1
    #
    #
    # aksesuarList = []
    # i = 0
    # for product in products:
    #
    #     if 'aksesuar' in product.category:
    #
    #         aksesuarList.append(product)
    #         i += 1


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



    context = {'products': products,'kadinList': kadinList,'erkekList': erkekList,'aksesuarList':aksesuarList,'categories':categories}
    return render(request, 'shop.html', context)



def seyirci(request):
    seyirci=Seyirci.objects.all()
    brands=Brands.objects.all()

    context ={'seyirci':seyirci,'brands':brands}
    return render(request, 'contact.html', context)



