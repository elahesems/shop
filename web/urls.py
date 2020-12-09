from django.urls import path

from web import views

urlpatterns =[
    path('',views.home,name="home"),
    path('seyirci/',views.seyirci,name="seyirci"),
    path('shop/',views.shop,name="shop"),
]