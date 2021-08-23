from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:username>', views.userhome, name="userhome"),
    path('<str:username>/userprofile', views.userprofile, name="userprofile"),
    path('<str:username>/cart', views.cart, name="cart"),
    path('<str:username>/cart/additem/<str:productname>',views.cart,name="additem")

]
