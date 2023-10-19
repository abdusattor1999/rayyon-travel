from django.shortcuts import render
from .models import Travel, Post

def home_page(request):
    travels = Travel.objects.filter(active=True).order_by("-id")[:4]
    return render(request, "home_page.html", {"travels":travels})


def about(request):
    return render(request, 'about_page.html')