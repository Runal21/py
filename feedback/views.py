from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from feedback.views import *
from django.contrib  import messages
from .models import Feedback, FeedbackReply, User


@login_required(login_url='/login/')
# Create your views here.
def feedback_submit(request):
    if request.method =="POST":
        fb_content = request.POST.get('fb_content')
 # Get the logged-in user
        fb_uname = request.user
        feedback = Feedback.objects.create(fb_uname=fb_uname, fb_content=fb_content)
        feedback.save()
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('home')  # Redirect to the home page after submitting feedback
    else:
        return render(request,'feedback/feedback_submit.html')

def admin_reply(request):
    replies = FeedbackReply.objects.all()
    return render(request, "feedback/userviewfeedback.html", {'replies': replies})

def user_feedback(request):
    user = request.user
    feedbacks = Feedback.objects.filter(fb_uname=user)
    return render(request, 'feedback/feedback_reply_form.html', {'feedbacks': feedbacks})