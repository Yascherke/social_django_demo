from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chats_list, name='chats_list'),
    path('chat/', include('chats.urls')),

]
