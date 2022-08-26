from django.views import generic

from .models import Project

class ProjectDetails(generic.DetailView):
    model = Project
    template_name = 'projects/details.html'
    lookup_field = 'slug'

    def get(self, *args, **kwargs):
        slug = kwargs.get('slug')
        project = Project.objects.get(slug=slug)

        if not self.request.user.is_authenticated:
            project.views += 1
            project.save()

        return super().get(*args, **kwargs)