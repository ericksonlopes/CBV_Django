from django.urls import path
from redirectview.views import RedirectCBV


urlpatterns = [
    path('', RedirectCBV.as_view(), name='my-view'),
]
