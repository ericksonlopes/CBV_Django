from django.urls import path

from createview.views import PersonCreateCBV

urlpatterns = [
    path('', PersonCreateCBV.as_view(), name='my-create'),
]
