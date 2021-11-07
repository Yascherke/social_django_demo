from django.urls import path, include
from . import views

app_name='chats'
urlpatterns = [
    path('', views.chats_list, name='index'),
    path('chat/', include('chats.urls')),

]
