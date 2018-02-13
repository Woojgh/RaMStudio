from django.urls import path
from .views import ProjectsView, ProjectCreateView

urlpatterns = [
    path('', ProjectsView.as_view(), name='project_list'),
    path('project_create/', ProjectCreateView.as_view(), name='project_create')
]