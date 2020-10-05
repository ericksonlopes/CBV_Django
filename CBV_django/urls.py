from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', include('view.urls')),
    path('templateview/', include('templateview.urls'), name='my-templateview'),
    path('detailview/', include('detailview.urls'), name='my-detailview'),
    path('listview/', include('listview.urls'), name='my-listview')
]
