from django.urls import path
from templateview.views import TemplateCBV

urlpatterns = [
    path('', TemplateCBV.as_view(), name='my-view'),
]
