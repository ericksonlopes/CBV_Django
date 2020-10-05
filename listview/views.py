from django.utils import timezone
from django.views.generic.list import ListView
from database.models import Person


class ListViewCBV(ListView):
    model = Person
    # paginação se caso tenha
    paginate_by = 100

    # Template especificado
    template_name = 'listview/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
