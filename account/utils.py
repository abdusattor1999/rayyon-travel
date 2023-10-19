from django.core.mail import send_mail
from django.conf import settings




def sendSimpleEmail(title,name:str, msg :str, contact:str, tour=None):
    subject = title
    message = f"Yuboruvchi : {name.title()}\nAloqa : {contact}\n\nXabar matni : \n{msg}"
    email_from = settings.EMAIL_HOST_USER
    recipient = ["rayhontour.agency@gmail.com"]
    ms = send_mail( subject, message, email_from, recipient)
    return True