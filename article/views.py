from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import AdminArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def article(request):
    return render(request,'article/article.html')

@staff_member_required
def admin_create_article(request):
    if request.method == 'POST':
        form = AdminArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = AdminArticleForm()
    return render(request, 'article/create_article.html', {'form': form})

@staff_member_required
def admin_update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = AdminArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = AdminArticleForm(instance=article)
    return render(request, 'article/update_article.html', {'form': form})
