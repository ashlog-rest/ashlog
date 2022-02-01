from django.urls import path, include
from api.views import LogView, ProjectView

urlpatterns = [
    path('log/', LogView.as_view()),
    path('project/', ProjectView.as_view()),
    path('project/<int:project_id>/', ProjectView.as_view()),
    path('project/<int:project_id>/log/', LogView.as_view()),
]
