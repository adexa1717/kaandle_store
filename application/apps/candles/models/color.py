from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractTimeModel, AbstractActivityModel


class Color(AbstractActivityModel, AbstractTimeModel, models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    hex_code = models.CharField(max_length=50, verbose_name=_("hex code"))

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')
