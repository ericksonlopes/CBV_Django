from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        """
            enviar e-mail usando o dicionário self.cleaned_data
        """
        pass
