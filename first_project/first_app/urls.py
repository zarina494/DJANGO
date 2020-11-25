from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('users/',userlist),
    path('blog/',bloglist),
    path('post/',postlist),
]