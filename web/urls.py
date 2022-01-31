from django.urls import path
from web.views import (
    delete_log_view,
    delete_project_view,
    edit_profile_view,
    edit_project_view,
    export_project_view,
    index_view,
    project_view,
    login_view,
    logout_view,
    new_project_view,
    register_view,
)

urlpatterns = [
    path('', index_view),
    path('log/delete/<int:log_id>/', delete_log_view),
    path('project/<int:project_id>/delete/', delete_project_view),
    path('project/<int:project_id>/edit/', edit_project_view),
    path('project/<int:project_id>/export/', export_project_view),
    path('project/<int:project_id>/', project_view),
    path('project/new/', new_project_view),
    path('profile/<str:username>/edit/', edit_profile_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
