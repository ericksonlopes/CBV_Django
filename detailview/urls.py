from django.urls import path
from detailview.views import DetailViewCBV


urlpatterns = [
    path('<int:pk>/', DetailViewCBV.as_view(), name='my-detailview'),
]
