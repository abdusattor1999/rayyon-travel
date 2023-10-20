from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from datetime import datetime

class Travel(models.Model):
    image = models.ImageField(upload_to='travel_images/%B/')
    title = models.CharField(max_length=150, verbose_name=_("Sarlavha"))
    departure = models.DateField(blank=True, null=True, verbose_name=_("Jo'nash sanasi"))
    desctiption = models.TextField(blank=True, null=True, verbose_name=_("Qo'shimcha malumot"))
    class_type = models.CharField(blank=True, null=True, max_length=100, verbose_name=_("Paket turi"))
    price = models.DecimalField(verbose_name=_("Narxi"), max_digits=11, decimal_places=2)
    active = models.BooleanField(default=True, verbose_name=_("Hozir mavjudmi"))
    
    def __str__(self) -> str:
        return f"{self.departure}: {self.title}"
    
    def get_departure_info(self):
        return f"Jo'nash : {self.departure.strftime('%d-%m-%Y')}"

    def get_absolute_url(self):
        return reverse("posts:travel_details", kwargs={"pk": self.pk})
    
class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Sarlavha"))
    body = models.TextField(blank=True, null=True, verbose_name=_("1 - Qism"))
    body2 = models.TextField(blank=True, null=True, verbose_name=_("2 - Qism"))
    image = models.ImageField(upload_to="post_pictures/%B/", blank=True, null=True)
    image2 = models.ImageField(upload_to="post_pictures/%B/", blank=True, null=True)
    views = models.PositiveIntegerField(default=0, verbose_name=_("Ko'rishlar soni"))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("posts:post_details", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title} : {self.created_at}"
    
    class Meta:
        verbose_name_plural = "Yangiliklar"
        verbose_name = "Yangilik"
    
