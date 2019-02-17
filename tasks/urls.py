from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout_user, name="logout"),
    path('login', views.login_user, name="login"),
]