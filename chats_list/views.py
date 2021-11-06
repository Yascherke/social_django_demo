from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chats_list(request):
    return render(request, "chats_list/index.html")