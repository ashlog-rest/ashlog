from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from api.models import Log, Project


def index_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {
        'user': request.user,
        'projects': Project.objects.filter(
            Q(users__in=[request.user])
        ),
    }
    return render(request, 'pages/index.html', context)


def project_view(request, project):
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {
        'logs': Log.objects.filter(
            project=project
        ),
        'project': Project.objects.get(
            Q(users__in=[request.user]),
            id=project,
        ),
    }
    return render(request, 'pages/project.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f'You are now logged in as {user.username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'pages/login.html', {'login_form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
