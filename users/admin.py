from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'first_name', 'second_name', 'joined_on')
    list_filter = ('user', 'joined_on')
    search_fields = ['user', 'first_name', 'second_name']

admin.site.register(UserProfile, UserProfileAdmin)