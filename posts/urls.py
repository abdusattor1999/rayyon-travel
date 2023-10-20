from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', home_page, name="home_page"),
    path('about-us/', about, name="about"),
    path('contact-us/', contact, name="contact"),
    path('news-list/', news_list, name="post_list"),
    path('news/<int:pk>/', post_details, name="post_details"),
]