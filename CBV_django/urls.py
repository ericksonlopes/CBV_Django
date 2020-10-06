from django.contrib import admin
from django.urls import path, include
from django.views.generic import ArchiveIndexView

from database.models import Article
from deleteview.views import DeleteViewCBV
from generic_date_views.views import DetailViewCBVarticle
from updateview.views import UpdateViewCBV

urlpatterns = [
    path('admin/', admin.site.urls),
    # base view
    # View básica
    path('view/', include('view.urls')),

    # retorna um template
    path('templateview/', include('templateview.urls'), name='my-templateview'),

    # Generic display views
    # detalhes de um determinado dado
    path('detailview/', include('detailview.urls'), name='my-detailview'),
    # lista os dados
    path('listview/', include('listview.urls'), name='my-listview'),

    # Generic editing views
    # formulario com cbv
    path('formview/', include('formview.urls'), name='my-formview'),
    # cria dados
    path('createview/', include('createview.urls'), name='my-createview'),
    # deleta dados
    path('deleteview/<int:pk>/', DeleteViewCBV.as_view(), name='my-deleteview'),
    # update dos dados
    path('updateview/<int:pk>/', UpdateViewCBV.as_view(), name='my-updateview'),

    # Generic date views
    # detalhes
    path('archiveindexbiew/<int:pk>', DetailViewCBVarticle.as_view(), name='detail-article'),

    # Objetos com uma data futura não são exibidos, a menos que você defina allow_futurecomo True.

    # exibe os dados mais recentes (menos futuro)
    path('archiveindexbiew/', ArchiveIndexView.as_view(model=Article, date_field="pub_date",
                                                       template_name='recentes/recentes.html'), name="article_archive"),

    # Exibe todos os dados do ano (menos futuro)

]
