from django.views.generic.edit import FormView

from formview.forms import ContactForm


class FormCBV(FormView):
    template_name = 'formview/form.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        """
            Este método é chamado quando dados de formulário válidos foram postados.
            Deve retornar um HttpResponse.
        """
        form.send_email()
        return super().form_valid(form)
