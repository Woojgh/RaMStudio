from django.urls import path
from .views import ProjectsView, ProjectCreateView, ProjectDetailView

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects'),
    path('project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('project_detail/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),
]