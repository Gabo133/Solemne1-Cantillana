from django.urls import path
from auth_basket import views

urlpatterns = [
    path('login', views.auth_login, name="auth_login"),
    path('logout', views.auth_logout, name="auth_logout"),
]
