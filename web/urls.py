from django.urls import path

from web import views

urlpatterns =[
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('seyirci/',views.seyirci,name="seyirci"),
    path('shop/',views.shop,name="shop"),
    path('shop/<str:productSpeciality>__<str:category>/',views.shop_detail,name="shop_detail"),
    path('about_us/',views.team_member,name="team_member"),
    path('product_details/<str:pk>/',views.product_details,name="product_details"),
]