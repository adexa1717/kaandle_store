from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractActivityModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def deactivate(self, ):
        self.is_active = False
        self.save()
        return self


class AbstractTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created date"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated date"))

    class Meta:
        abstract = True
