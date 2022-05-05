from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractActivityModel, AbstractTimeModel


class FormImages(models.Model):
    path = models.ImageField()


class Form(AbstractActivityModel, AbstractTimeModel, models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    images = models.ForeignKey(to=FormImages, on_delete=models.CASCADE, related_name="forms")
