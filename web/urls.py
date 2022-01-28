from django.urls import path
from web.views import (
    index_view,
    project_view,
    login_view,
    logout_view,
    new_project_view,
    search_project_view,
)

urlpatterns = [
    path('', index_view),
    path('project/<project_id>/', project_view),
    path('project/<project_id>/<page_number>', project_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('new/', new_project_view),
    path('search/', search_project_view),
]
