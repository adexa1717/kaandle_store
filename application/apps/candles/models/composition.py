from django.db import models
from django.utils.translation import gettext_lazy as _


class Composition(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    class Meta:
        verbose_name = _('composition')
        verbose_name_plural = _('compositions')
