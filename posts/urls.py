from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', home_page, name="home_page"),
    path('about-us/', about, name="about")
] 