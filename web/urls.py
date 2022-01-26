from django.urls import path
from web.views import (
    index_view,
    login_view,
    logout_view,
    project_view,
)

urlpatterns = [
    path('', index_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('project/<project>/', project_view),
]
