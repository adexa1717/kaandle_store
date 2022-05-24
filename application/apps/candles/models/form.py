from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractActivityModel, AbstractTimeModel


class CandleForm(AbstractActivityModel, AbstractTimeModel, models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))


class CandleFormImage(models.Model):
    path = models.ImageField()
    images = models.ForeignKey(to=CandleForm, on_delete=models.CASCADE, related_name="images")
