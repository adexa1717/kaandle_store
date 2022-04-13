from django.http import HttpResponse
from django.shortcuts import render


def current_datetime(request):
    html = "<html><body>Hello world!</body></html>"
    return HttpResponse(html)
