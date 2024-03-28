from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feedback(request):
    return render(request,'feedback/feedback.html')
