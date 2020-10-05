from django.shortcuts import render
from django.views.generic import TemplateView

from database.models import Person


class TemplateCBV(TemplateView):
    # nome do template
    template_name = 'templateview/templateview.html'

    # implementando dados através de um context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # inserindo uma variavel
        context['person'] = Person.objects.all()[:5]
        return context
