from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login/',views.login_view,name='login_view'),
    path('accounts/register/',views.register_view,name='register_view'),
]