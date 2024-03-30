from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback
from feedback.views import *

# Create your views here.
def feedback_send(request):
    if request.method =="POST":
        fb_uname=request.POST.get('fb_uname')
        fb_type = request.POST.get('fb_type')
        fb_content = request.POST.get('fb_content')
        
        fb_name =Feedback.objects.filter(fb_uname=fb_uname)
        if fb_name not in Feedback:
            return HttpResponse("Cannot make any feddback")
    
        fb_submit = Feedback.objects.create(fb_uname=fb_uname ,fb_type=fb_type ,fb_content=fb_content)
        fb_submit.save()
    return render(request,'feedback/feedback.html')

    