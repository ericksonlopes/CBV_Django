from django.urls import path

from view.views import MyView

urlpatterns = [
    path('', MyView.as_view(), 'view'),
]
