from django.views.generic.detail import DetailView
from django.utils import timezone

from database.models import Person


class DetailViewCBV(DetailView):
    model = Person
    template_name = 'detailview/detailview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

