# Generated by Django 3.2.12 on 2022-02-12 12:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import slugger.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', slugger.fields.AutoSlugField(populate_from='title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Health & Fitness', 'Health & Fitness'), ('Lifestyle', 'Lifestyle'), ('Fashion & Beauty', 'Fashion & Beauty'), ('Software & Coding', 'Software & Coding'), ('Tech & Gadgets', 'Tech & Gadgets'), ('DIY Craft', 'DIY Craft'), ('Parenting', 'Parenting'), ('Music', 'Music'), ('Art & Design', 'Art & Design'), ('Books & Writing', 'Books & Writing'), ('Personal Finance', 'Personal Finance'), ('Interior Design', 'Interior Design'), ('Sports', 'Sports'), ('News', 'News'), ('Movies', 'Movies')], max_length=200)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('article_author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='users.userprofile')),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
    ]
