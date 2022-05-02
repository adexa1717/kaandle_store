from django.db import models
from django.utils.translation import gettext_lazy as _


class FormImages(models.Model):
    path = models.ImageField()


class Form(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    images = models.ForeignKey(to=FormImages, on_delete=models.CASCADE, related_name="forms")
