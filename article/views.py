from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def article(request):
    articles = Article.objects.all()
    return render(request, 'article/article.html', {'articles': articles})

@staff_member_required
def admin_create_article(request):
    if request.method == 'POST':
        art_title = request.POST.get('art_title')
        art_author =request.POST.get("art_author")
        art_content = request.POST.get('art_content')
        art_image =request.FILES.get('art_image')
            
        # Create the article object
        art = Article.objects.create(art_title=art_title, art_content=art_content, art_author=art_author, art_image=art_image)
        art.save()

        # Redirect to the list of articles after successful creation
        return redirect('article')
    else:
        return render(request, 'article/create_article.html')
    

