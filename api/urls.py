from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from api import views

urlpatterns = [
    path('index/', views.index, name="API Index")
]
