from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.serializers import serialize
from django.core.paginator import Paginator
from authentication.models import User
from api.models import Log, Project
from api.serializers import LogSerializer
from web.forms import LoginForm, RegisterForm


def delete_log_view(request, log_id=None):
    """ Delete log object """
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        if not log_id is None:
            log = Log.objects.get(id=log_id)
            project = log.project
            if request.user in project.users.all():
                log.delete()
                return redirect(f'/project/{project.id}')
    return redirect('/')


def delete_project_view(request, project_id=None):
    """ Delete log object """
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        if not project_id is None:
            project = Project.objects.get(id=project_id)
            if request.user in project.users.all():
                project.delete()
    return redirect('/')


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
    ).order_by('-created')
    paginator = Paginator(logs, 15)
    if page_number < 1:
        page_number = 1
    elif page_number > paginator.num_pages:
        page_number = paginator.num_pages
    logs = paginator.get_page(page_number)
    context = {
        'logs': serialize('json', logs),
        'project': Project.objects.get(
            Q(users__in=[request.user]),
            id=project_id,
        ),
        'page': {
            'current': page_number,
            'num_pages': paginator.num_pages,
        },
    }
    return render(request, 'pages/project.html', context)


def login_view(request):
    """ View for login page """
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('/')
    return render(request, 'pages/login.html')


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


def register_view(request):
    """ View for user registration """
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('/')
    return render(request, 'pages/register.html')


def search_project_view(request):
    """ View for searching projects """
    if not request.user.is_authenticated:
        return redirect('/login/')
    project_name = request.GET.get('q')
    if not project_name:
        project_name = ''
    projects = Project.objects.filter(
        Q(users__in=[request.user]),
        name__contains=project_name,
    )
    context = {
        'projects': projects,
        'query': project_name,
    }
    return render(request, 'pages/search.html', context)
