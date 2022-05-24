from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractTimeModel, AbstractActivityModel


class Candle(AbstractActivityModel, AbstractTimeModel, models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    height = models.PositiveSmallIntegerField(verbose_name=_("height"))
    width = models.PositiveSmallIntegerField(verbose_name=_("width"))
    composition = models.ForeignKey(to="candles.Composition", on_delete=models.SET_NULL, null=True,
                                    related_name="candles", verbose_name=_("composition"))
    form = models.ForeignKey(to="candles.CandleForm", on_delete=models.SET_NULL, null=True,
                             related_name="candles", verbose_name=_("form"))
    wick = models.ForeignKey(to="candles.Wick", on_delete=models.SET_NULL, null=True,
                             related_name="candles", verbose_name=_("wick"))
    color = models.ForeignKey(to="candles.Color", on_delete=models.SET_NULL, null=True,
                              related_name="candles", verbose_name=_("color"))
    smell = models.ForeignKey(to="candles.Smell", on_delete=models.SET_NULL, null=True,
                              related_name="candles", verbose_name=_("smell"))

    class Meta:
        verbose_name = _('candle')
        verbose_name_plural = _('candles')


class CandleImages(models.Model):
    path = models.ImageField()
    images = models.ForeignKey(to=Candle, on_delete=models.CASCADE, related_name="images")
