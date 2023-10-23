from django.shortcuts import render, redirect
from .forms import CustomerForm
from.utils import sendSimpleEmail
from posts.models import Travel
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from account.models import Customer

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('posts:home_page')
            else:
                context = {
                'success' : False,
                'message' : "Berilgan malumotlar bo'yicha Foydalanuvchi profili topilmadi \"Username\" yoki \"Parol\" xato bo'lishi mumkin tekshirib qaytadan kiriting !",
                }
                return render(request, 'notifications.html', context)
            
        else:
            context = {
            'success' : False,
            'message' : "Berilgan malumotlar bo'yicha Foydalanuvchi profili topilmadi \"Username\" yoki \"Parol\" xato bo'lishi mumkin tekshirib qaytadan kiriting !",
            }
            return render(request, 'notifications.html', context)
        
    else:
        form = LoginForm()
        return render(request, 'login_form.html', {'form':form})

def create(request, id=None):
    if request.method == "POST":
        form = CustomerForm(data=request.POST)

        if form.is_valid():
            
            all_data = form.cleaned_data
            name = all_data.get("full_name", None)
            phone = all_data.get("phone", None)
            travel = Travel.objects.filter(id=id).last()
            all_data['travel'] = travel
            title = "Sayohatga ariza !"
            msg = f"{travel.title} - {travel.get_departure_info()} Touriga buyurtma"
            try:
                Customer.objects.create(**all_data)
                sendSimpleEmail(
                title, name, msg, phone
                )
            except:
                pass
            context = {
                'success':True,
                "status":200,
                "message":_("Arizangiz yuborildi tez orada aloqaga chiqamiz !")
            }
            return render(request, "notifications.html", context)
    else:
        context = {
            "pk":id,
            "form":CustomerForm()
        }
        return render(request, "register_form.html", context)

def private_page(request):
    return render(request, 'kabinet.html')