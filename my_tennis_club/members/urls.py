from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Homepage, name='homepage'),
    path('', views.sign, name='signup'),
    path('login', views.login_page, name='login'),
    path('logout',views.Logoutpage,name='logout')

]
