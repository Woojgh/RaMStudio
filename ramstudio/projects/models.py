"""Photo and Album models created by a User."""
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone
from sorl.thumbnail import ImageField


class Photo(models.Model):
    """Photo uploaded by a User."""

    image = ImageField(upload_to='images')
    title = models.CharField(max_length=180, blank=True, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The string from of the image."""
        return self.title


class Project(models.Model):
    """Album of Photos created by the User."""

    photos = models.ManyToManyField(Photo, related_name='projects')
    title = models.CharField(max_length=180, blank=True, default='Untitled')
    cover = models.ForeignKey(Photo, blank=True, null=True, related_name='+', on_delete='CASCADE')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The string from of the project."""
        return self.title


class ProjectForm(ModelForm):
    """Form for an Project."""

    class Meta:
        """Meta."""

        model = Project
        fields = ['title', 'description', 'photos', 'cover']

    # def __init__(self, *args, **kwargs):
        # """Limit photos to only those by the user."""
        # super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['photos'].queryset = Photo.objects.all()
        # self.fields['cover'].queryset = Photo.objects.all()