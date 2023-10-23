from django.shortcuts import render
from .models import Travel, Post
from account.models import Customer
from account.utils import sendSimpleEmail
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def home_page(request):
    travels = Travel.objects.filter(active=True).order_by("-id")[:4]
    # trans = translate('ru')
    return render(request, "home_page.html", {"travels":travels})

# def translate(language):
#     cur_lang = get_language()
#     try:
#         activate(language)
#     finally:
#         activate(cur_lang)
    

def about(request):
    return render(request, 'about_page.html')

def contact(request):
    if request.method == "POST":
        data_from_user = request.POST
        full_name = data_from_user.get('full_name', None)
        phone = data_from_user.get('phone', None)
        comment = data_from_user.get('message', None)
        if full_name == "" or phone == "":
            context = {
                "success":False,
                "status":400,
                "message":_("'Ism-Familiya' va 'Telefon' kiritilishi kerak !")
            }
            return render(request, 'notifications.html', context)
        else:
            Customer.objects.create(
                full_name=full_name,
                phone=phone,
                comment=comment
            )
            title = "Foydalanuvchidan xabar !"
            name = full_name
            phone = phone
            msg = comment
            sendSimpleEmail(
                title, name, msg, phone
            )
            context = {
                'success':True,
                "status":200,
                "message":"Xabaringiz yuborildi !"
            }
            return render(request, "notifications.html", context)
    return render(request, 'contact_page.html')

def news_list(request):
    news = Post.objects.all().order_by("-created_at")[:10]
    return render(request, "post_list.html", {"news":news})

def post_details(request, pk):
    post = Post.objects.filter(id=pk).last()
    if post:
        post.views += 1
        post.save()
        return render(request, "post_details.html", {"post":post})
    else:
        data = {
            "success":False,
            "message":_("Berilgan ID raqamli Yangilik mavjud emas !"),
            "status":400
        }
        return render(request, "notifications.html", data)
