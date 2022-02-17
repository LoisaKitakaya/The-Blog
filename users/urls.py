from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('new_login/', login_new_user, name='login_new_user'),
    path('profile/', profile, name='profile'),
    path('new_profile/', new_profile, name='new_profile'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
    path('user/<int:id>/', other_user_profile, name='other_user_profile'),
    path('logout/', logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)