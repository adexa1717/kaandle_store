from django.db import models
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):
    is_active = models.BooleanField()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
