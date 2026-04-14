from django.urls import path 
from .views import register, login, hello_api, CustomTokenRefreshView

urlpatterns = [
    path("register/",register),
    path("login/",login),
    path('hello/',hello_api),

    path("token/refresh/",CustomTokenRefreshView.as_view(),name="token_refresh"),
]

