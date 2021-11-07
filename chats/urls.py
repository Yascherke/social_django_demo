from django.urls import path, include
from . import views

app_name='chat'
urlpatterns = [
    path('', views.chat, name='index'),

]
