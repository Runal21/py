from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def DESagent(request):
    return render(request, "DESagent/DESagent.html")