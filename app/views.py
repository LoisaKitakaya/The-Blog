from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):

    all_articles = Article.objects.select_related('article_author').all()

    page_title = 'All articles'

    context = {
        'articles' : all_articles,
        'page_title' : page_title,
    }

    return render(request, 'app/index.html', context)

def search_db(request):

    page_title = 'Search results'

    current_user = request.user

    if request.method == 'GET':

        query = request.GET.get('q')

        search_result = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(category__icontains=query))

        if search_result is None == True:

            search_result = User.objects.filter(Q(username__icontains=query))

        elif search_result is None ==True:

            search_result = Comment.objects.filter(Q(comment__icontains=query))

    else:

        search_result = []

    context = {
        'page_title' : page_title,
        'search_articles' : search_result,
        'current_user' : current_user,
    }

    return render(request, 'app/search.html', context)

def view_article(request, slug):

    current_user = request.user

    full_article = Article.objects.get(slug=slug)

    article_comments = Comment.objects.select_related('comment_author').filter(comment_article=full_article)

    if request.method == 'POST':

        form = PostComment(request.POST)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.comment_author = current_user

            save_action.comment_article = full_article

            save_action.save()

            messages.success(request, 'Comment posted successfully.')

    else:

        form = PostComment()

    context = {
        'article' : full_article,
        'all_comments' : article_comments,
        'form' : form,
    }

    return render(request, 'app/full_article.html', context)

def all_user_articles(request):

    current_user = request.user

    all_articles = Article.objects.select_related('article_author').filter(article_author=current_user)

    context = {
        'articles' : all_articles
    }

    return render(request, 'app/all_user_articles.html', context)

@login_required(login_url='login')
def dashboard(request):

    current_user = request.user

    context = {
        'this_user' : current_user,
    }

    return render(request, 'app/dashboard.html', context)

@login_required(login_url='login')
def post_article(request):

    current_user = request.user

    breadcrumb_title = 'Create Article'

    if request.method == 'POST':

        form = PostArticle(request.POST, request.FILES)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.article_author = current_user

            save_action.save()

            messages.success(request, 'Article created.')
            
        return redirect('home')

    else:

        form = PostArticle()

    context = {
        'form' : form,
        'breadcrumb_title' : breadcrumb_title,
    }

    return render(request, 'app/post_article.html', context)

@login_required(login_url='login')
def update_article(request, slug):

    current_user = request.user

    article_to_update = Article.objects.get(slug=slug)

    breadcrumb_title = 'Update/Edit Article'

    update_breadcrumb = True

    if request.method == 'POST':

        form = PostArticle(request.POST, request.FILES, instance=article_to_update)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.article_author = current_user

            save_action.save()

            messages.info(request, 'Article updated.')
            
        return redirect('home')

    else:

        form = PostArticle()

    context = {
        'form' : form,
        'breadcrumb_title' : breadcrumb_title,
        'update_breadcrumb' : update_breadcrumb
    }

    return render(request, 'app/post_article.html', context)

@login_required(login_url='login')
def delete_article(request, id):

    article_to_delete = Article.objects.get(id=id)
    
    article_to_delete.delete()

    messages.error(request, 'Article deleted')

    return redirect('all_articles')

def about(request):

    return render(request, 'app/about.html')