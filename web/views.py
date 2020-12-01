from django.shortcuts import render, redirect


# Create your views here.
from web.models import *


def home(request):
    sliders=Sliders.objects.all()
    products = Product.objects.all()
    categoriesList = Product._meta.get_field('category').choices
    categories=[]
    for i in categoriesList:
        categories.append(i[0])
    context = {'sliders':sliders,'products':products,'categories':categories}
    return render(request,'index.html',context)