from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.serializers import serialize
from api.models import Log, Project
from api.serializers import LogSerializer
from web.forms import LoginForm


def index_view(request):
    """ View for homepage """
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {
        'user': request.user,
        'projects': Project.objects.filter(
            Q(users__in=[request.user])
        ),
    }
    return render(request, 'pages/index.html', context)


def project_view(request, project_id, page_number=1):
    """ View for project """
    if not request.user.is_authenticated:
        return redirect('/login/')
    logs = Log.objects.filter(
        project=project_id
    )
    context = {
        'logs': serialize('json', logs),
        'project': Project.objects.get(
            Q(users__in=[request.user]),
            id=project_id,
        ),
        'page': page_number,
    }
    return render(request, 'pages/project.html', context)


def login_view(request):
    """ View for login page """
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('/')
    form = LoginForm()
    return render(request, 'pages/login.html', {'login_form': form})


def logout_view(request):
    """ View for logout """
    logout(request)
    return redirect('/')


def new_project_view(request):
    """ Handle creation of a new project """
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        project_name = request.POST.get('project-name')
        project = Project.objects.create(
            name=project_name,
        )
        project.users.add(request.user)
        project.save()
        return redirect(f'/project/{project.id}')
    return redirect('/')


def search_project_view(request):
    """ View for searching projects """
    if not request.user.is_authenticated:
        return redirect('/login/')
    project_name = request.GET.get('q')
    if not project_name:
        project_name = ''
    projects = Project.objects.filter(
        name__contains=project_name,
    )
    context = {
        'projects': projects,
        'query': project_name,
    }
    return render(request, 'pages/search.html', context)
