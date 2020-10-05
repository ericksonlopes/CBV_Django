from django.urls import path

from listview.views import ListViewCBV

urlpatterns = [
    path('', ListViewCBV.as_view(), name='my-listview-app'),
]
