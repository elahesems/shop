from django.urls import path

from web import views

urlpatterns =[
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('seyirci/',views.seyirci,name="seyirci"),
    path('shop/',views.shop,name="shop"),
    path('about-us/',views.about,name="about"),
]