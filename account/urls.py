from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('register-to/<int:id>', create, name="register"),
    path('register-to/', create, name="register"),
] 