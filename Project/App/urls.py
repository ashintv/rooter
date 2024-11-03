from django.urls import path
from . import views

urlpatterns = [
    path(route= 'home', view= views.home_page_view, name='home'),
]