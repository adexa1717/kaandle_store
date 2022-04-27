from django.contrib.auth.views import LoginView
from django.http import HttpResponse


def current_datetime(request):
    html = "<html><body>Hello world!</body></html>"
    return HttpResponse(html)


class CustomUserLoginView(LoginView):
    template_name = "auth/login.html"
    next_page = "/"
