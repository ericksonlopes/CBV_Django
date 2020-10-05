from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from database.models import Person


class PersonCreateCBV(CreateView):
    template_name = 'createview/person_form.html'
    model = Person
    fields = ['nome', 'sobrenome']
    success_url = reverse_lazy('my-listview-app')
