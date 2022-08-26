from django.views import generic

from projects.models import Project
from skills.models import Skill
from main.models import CV

class IndexView(generic.ListView):
    model = Project
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['frontend'] = Skill.objects.filter(category__name__icontains='frontend')
        context['backend'] = Skill.objects.filter(category__name__icontains='backend')
        context['other'] = Skill.objects.filter(category__name__icontains='other')
        context['cv'] = CV.objects.first()
        return context


class Error404View(generic.TemplateView):
    template_name = '_404.html'

error_404_view = Error404View.as_view()