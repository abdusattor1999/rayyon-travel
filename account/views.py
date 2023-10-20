from django.shortcuts import render
from .forms import CustomerForm
from.utils import sendSimpleEmail
from posts.models import Travel

def create(request, id=None):
    if request.method == "POST":
        form = CustomerForm(data=request.POST)

        if form.is_valid():
            form.save()
            all_data = form.cleaned_data
            name = all_data.get("full_name", None)
            phone = all_data.get("phone", None)
            pk = request.POST.get('pk')
            travel = Travel.objects.filter(id=pk).last()
            title = "Sayohatga ariza !"
            msg = f"{travel.title} - {travel.get_departure_info()} Touriga buyurtma"


            sendSimpleEmail(
                title, name, msg, phone
            )
            context = {
                'success':True,
                "status":200,
                "message":"Arizangiz yuborildi tez orada aloqaga chiqamiz !"
            }
            return render(request, "notifications.html", context)
    else:
        context = {
            "pk":id,
            "form":CustomerForm()
        }
        return render(request, "register_form.html", context)
