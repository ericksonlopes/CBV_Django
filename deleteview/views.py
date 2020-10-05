from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from database.models import Person


class DeleteViewCBV(DeleteView):
    model = Person
    success_url = reverse_lazy('my-listview-app')
    template_name = 'deleteview/person_delete_confirm.html'
