from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_account', views.create_account)
]
