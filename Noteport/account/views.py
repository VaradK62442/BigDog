from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

from account.forms import UserForm, UserProfileForm
from account.models import UserProfile


@login_required
def index(request):
    return render(request, 'account/index.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('account:index'))
            else:
                return redirect(reverse('account:login'))
            
        else:
            return redirect(reverse('account:login'))
    
    else:
        return render(request, 'account/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('account:index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.profilePicture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
        request,
        'account/register.html',
        context={
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        }
    )