from django.urls import path, include
from . import views

app_name='chat'
urlpatterns = [
    path('', views.chats, name='index'),

]
