from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chats(request):
    return render(request, "chats/index.html")