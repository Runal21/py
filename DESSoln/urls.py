"""
URL configuration for DESSoln project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from forumpost.views import *
from feedback.views import *
from article.views import *
from DESagent.views  import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home,name='home'), #Home page
    path('register/',registerpage,name='register'),
    path('login/',loginpage,name='login'),
    path('logout/',logoutpage,name='logout'),
    path('about/',about,name="about"),#About page
    path('contact',contact,name="contact"),#Contact us page


    path('feedbacksubmit/',feedback_submit,name="feedback_submit"),#Feed
    path('admin_reply/', admin_reply, name='admin_reply'),
     path('user_feedback/', user_feedback, name='user_feedback'),
    

    path('article/',article, name= 'article'),#Article Page
    path('createarticle/',admin_create_article,name='create_article'),

    path('forumpost/',forumpost, name='forumpost'),#Discussion Forum



    path('DESagent/',DESagent, name='DESagent'),#Interact with DES



    path('admin/', admin.site.urls) 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

