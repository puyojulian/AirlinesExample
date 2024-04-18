from django.urls import path

from . import views

app_name = 'app_users'

urlpatterns = [
  path("", views.index, name="index"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("to_flights", views.reverse_to_flights, name="to_flights")
]