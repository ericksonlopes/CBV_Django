from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from database.models import Person


class UpdateViewCBV(UpdateView):
    model = Person
    fields = ['nome', 'sobrenome']
    template_name_suffix = '_update_form'
    template_name = 'updateview/person_update_form.html'
    success_url = reverse_lazy('my-listview-app')
