
from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("login/",views.login, name="login"),
    path("request/",views.add_request, name="add_request"),
  path("contact/",views.contact_us, name="contact_us"),
]
