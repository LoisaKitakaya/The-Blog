from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('article_author', 'title', 'category', 'posted_on')
    list_filter = ('article_author', 'category', 'posted_on')
    search_fields = ['article_author', 'category', 'title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('comment_author', 'posted_on')
    list_filter = ('comment_author', 'posted_on')
    search_fields = ['comment_author', 'comment']

admin.site.register(Comment, CommentsAdmin)