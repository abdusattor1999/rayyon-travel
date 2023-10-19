# Views
from django.shortcuts import render
from .forms import CustomerForm
from.utils import sendSimpleEmail

def create(request):
    if request.method == "POST":
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()

            all_data = form.cleaned_data
            title = all_data.get('title',None)
            name = all_data.get("full_name", None)
            phone = all_data.get("phone", None)
            msg = all_data.get("comment", None)
            tour = all_data.get("travel", None)
            if tour:
                tour = tour.title
            sendSimpleEmail(
                title, name, msg, phone, tour
            )
    
    return render(request, "home.html")
