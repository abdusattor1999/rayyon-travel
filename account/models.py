from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("To'liq ism sharif"))
    phone = models.CharField(max_length=50, verbose_name=_("Telefon raqami"), blank=True, null=True)
    travel = models.ForeignKey("posts.Travel", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name