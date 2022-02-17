from django.db import models
from django.contrib.auth.models import User
from slugger import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

CATEGORIES = (
    ('Food', 'Food'),
    ('Travel', 'Travel'),
    ('Health & Fitness', 'Health & Fitness'),
    ('Lifestyle', 'Lifestyle'),
    ('Fashion & Beauty', 'Fashion & Beauty'),
    ('Software & Coding', 'Software & Coding'),
    ('Tech & Gadgets', 'Tech & Gadgets'),
    ('DIY Craft', 'DIY Craft'),
    ('Parenting', 'Parenting'),
    ('Music', 'Music'),
    ('Art & Design', 'Art & Design'),
    ('Books & Writing', 'Books & Writing'),
    ('Personal Finance', 'Personal Finance'),
    ('Interior Design', 'Interior Design'),
    ('Sports', 'Sports'),
    ('News', 'News'),
    ('Movies', 'Movies')
)
class Article(models.Model):

    article_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profiles', blank=True)
    title = models.CharField(max_length=200, unique=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    content = RichTextUploadingField()
    category = models.CharField(max_length=200, choices=CATEGORIES)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-posted_on']

    def __str__(self):

        return self.title

class Comment(models.Model):

    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_of_comment', blank=True)
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_of_comment', blank=True)
    comment = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-posted_on']

    def __str__(self):

        return self.comment
