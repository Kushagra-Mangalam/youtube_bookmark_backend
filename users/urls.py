from django.urls import path 
from .views import register, login, hello_api
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/",register),
    path("login/",login),
    path('hello/',hello_api),

    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
]

