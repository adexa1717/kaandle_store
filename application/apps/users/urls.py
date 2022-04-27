from django.urls import path

from users import views

urlpatterns = [
    path('', views.current_datetime),
    path('login', views.CustomUserLoginView.as_view()),
]
