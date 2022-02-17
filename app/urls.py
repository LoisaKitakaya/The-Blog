from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_article', post_article, name='post_article'),
    path('update_article/<slug:slug>/', update_article, name='update_article'),
    path('dashboard/', dashboard, name='dashboard'),
    path('article/<slug:slug>/', view_article, name='view_article'),
    path('your_articles/', all_user_articles, name='all_articles'),
    path('delete_article/<int:id>/', delete_article, name='delete_article'),
    path('about/', about, name='about'),
    path('search/', search_db, name='search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)