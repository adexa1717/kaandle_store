from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractTimeModel, AbstractActivityModel


class Smell(AbstractActivityModel, AbstractTimeModel, models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    class Meta:
        verbose_name = _('smell')
        verbose_name_plural = _('smells')
