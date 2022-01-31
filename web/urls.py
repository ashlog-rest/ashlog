from django.urls import path
from web.views import (
    delete_log_view,
    delete_project_view,
    index_view,
    project_view,
    login_view,
    logout_view,
    new_project_view,
    register_view,
)

urlpatterns = [
    path('', index_view),
    path('delete/log/<int:log_id>/', delete_log_view),
    path('delete/project/<int:project_id>/', delete_project_view),
    path('project/<project_id>/', project_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('new/', new_project_view),
    path('register/', register_view),
]
