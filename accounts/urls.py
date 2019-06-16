from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_def,name='login_url'),
    path('logout/',logout_def,name='logout_url'),
    path('signup/',signup_def,name='signup_url'),
    path('password_change/',password_change,name='password_change_url'),
]
