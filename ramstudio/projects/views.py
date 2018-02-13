from django.shortcuts import render
from projects.models import Project
# from .forms import ProjectUploadForm, EditImageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.views import View


class ProjectsView(ListView):
    """Render all public album as gallery."""

    model = Project