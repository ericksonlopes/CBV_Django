from django.views.generic import RedirectView


class RedirectCBV(RedirectView):
    permanent = False
    query_string = True
    pattern_name = ''
