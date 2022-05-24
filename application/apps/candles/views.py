from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from candles.models import Color


class ColorView(ListView):
    model = Color
