from django.urls import path

from formview.views import FormCBV

urlpatterns = [
    path('', FormCBV.as_view(), name='my-form'),
]
