from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def forumpost(request):
    return render(request,'forumpost/forumpost.html')
