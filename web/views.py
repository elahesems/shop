from django.shortcuts import render, redirect


# Create your views here.
from web.models import Sliders


def home(request):
    sliders=Sliders.objects.all()
    context = {'sliders':sliders}
    return render(request,'index.html',context)