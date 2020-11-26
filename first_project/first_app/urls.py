from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import *



urlpatterns = [
    path('users/',userlist),
    path('blog/',bloglist),
    path('post/',postlist),
    path('blog/<int:blog_id>/',blogDetailView),

]