from django.contrib import admin
from django.urls import path, include

from deleteview.views import DeleteViewCBV
from updateview.views import UpdateViewCBV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('view/', include('view.urls')),

    path('templateview/', include('templateview.urls'), name='my-templateview'),

    path('detailview/', include('detailview.urls'), name='my-detailview'),

    path('listview/', include('listview.urls'), name='my-listview'),

    path('formview/', include('formview.urls'), name='my-formview'),

    path('createview/', include('createview.urls'), name='my-createview'),

    path('deleteview/<int:pk>/', DeleteViewCBV.as_view(), name='my-deleteview'),

    path('updateview/<int:pk>/', UpdateViewCBV.as_view(), name='my-updateview'),
]
