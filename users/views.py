from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib.auth.models import User
from .forms import *
from .models import UserProfile
from app.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Your new account has been created.')

            return redirect('login_new_user')

        else:

            for msg in form.error_messages:
                    
                print(form.error_messages[msg])

    else:

        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)

def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            messages.success(request, 'Successfully logged in.')

            return redirect('home')

    else:

        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/login.html', context)

def login_new_user(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            messages.info(request, 'Create a profile for your account.')

            return redirect('new_profile')

    else:

        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/login.html', context)

def logout_user(request):

    django_logout(request)

    messages.error(request, 'You have been logged out.')

    return redirect('home')

@login_required(login_url='login')
def profile(request):

    current_user = request.user

    user_profile = UserProfile.objects.get(pk=current_user.id)

    page_title = 'Your Profile Summary'

    context = {
        'user_details' : user_profile,
        'page_title' : page_title,
        'this_user' : current_user,
    }

    return render(request, 'users/profile_details.html', context)

def other_user_profile(request, id):

    user_profile = UserProfile.objects.get(pk=id)

    page_title = 'Profile Summary for: ' + str(user_profile)

    this_user = User.objects.get(id=id)

    user_articles = Article.objects.filter(article_author=this_user)

    page_subtitle = 'Articles by this User:'

    context = {
        'user_details' : user_profile,
        'page_title' : page_title,
        'user_articles' : user_articles,
        'page_subtitle' : page_subtitle,
        'this_user' : this_user,
    }

    return render(request, 'users/profile_details.html', context)

@login_required(login_url='login')
def new_profile(request):

    current_user = request.user

    page_title = 'Create New User Profile'

    breadcrumb_title = 'New Profile'

    if request.method == 'POST':

        form = CreateProfile(request.POST, request.FILES)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.user = current_user

            save_action.save()

            messages.info(request, 'New profile created.')
            
        return redirect('home')

    else:

        form = CreateProfile()

    context = {
        'form' : form,
        'page_title' : page_title,
        'breadcrumb_title' : breadcrumb_title,
    }

    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def update_profile(request, id):

    current_user = request.user

    user_profile = UserProfile.objects.get(pk=id)

    page_title = 'Update/Edit User Profile'

    breadcrumb_title = 'Update/Edit Profile'

    if request.method == 'POST':

        form = CreateProfile(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.user = current_user

            save_action.save()

            messages.info(request, 'Profile updated.')
            
        return redirect('dashboard')

    else:

        form = CreateProfile()

    context = {
        'form' : form,
        'page_title' : page_title,
        'breadcrumb_title' : breadcrumb_title,
    }

    return render(request, 'users/profile.html', context)