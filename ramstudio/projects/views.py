from django.shortcuts import render
from projects.models import Project, Photo, ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView,CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy


class ProjectsView(ListView):
    """Render all projects."""

    context_object_name = 'projects'
    template_name = 'projects.html'
    queryset = Project.objects.all()

    def get_context_data(self):
        context = super(ProjectsView, self).get_context_data()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Create a new project and store in the database."""

    template_name = 'project_create.html'
    login_url = reverse_lazy('home')
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')

    def get_form_kwargs(self):
        """Update the kwargs to include the current user's username."""
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """Assign user as creater of project."""
        form.instance.user = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDetailView(DetailView):
    """Render the project detail page."""

    template_name = 'project_detail.html'
    model = Project
    pk_url_kwarg = 'id'

    def get_object(self):
        """Get the project object by primary key and check if is public."""
        return super(ProjectDetailView, self).get_object()