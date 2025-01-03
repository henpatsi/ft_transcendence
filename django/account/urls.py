from django.urls import path
from . import views

urlpatterns = [
    path('', views.account),
    path('create_account/', views.create_account),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
