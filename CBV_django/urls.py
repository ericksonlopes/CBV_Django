from django.contrib import admin
from django.urls import path, include
from django.views.generic import ArchiveIndexView, DateDetailView

from database.models import Article
from deleteview.views import DeleteViewCBV
from generic_date_views.views import DetailViewCBVarticle, ArticleYearView, ArticleMonthView, \
    ArticleWeekView, ArticleDayView, ArticleToDay
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

    # exibe os dados mais generic_date_view
    path('archiveindexbiew/', ArchiveIndexView.as_view(model=Article, date_field="pub_date",
                                                       template_name='generic_date_view/generic_date_view.html'),
         name="article_archive"),

    # Exibe todos os dados do ano ano/
    path('archiveyear/<int:year>/', ArticleYearView.as_view(), name='article_year'),

    # exibir registros por ano e mes ano/mes
    path('archive/<int:year>/<int:month>/', ArticleMonthView.as_view(month_format='%m'), name='article_Month_numeric'),

    # exibir por semana ano/mes/semana
    path('archive_week/<int:year>/<int:month>/<int:week>/', ArticleWeekView.as_view(), name='article_week_numeric'),

    # exibir por dia ano/mes/dia
    path('archive_day/<int:year>/<int:month>/<int:day>/', ArticleDayView.as_view(month_format='%m'),
         name='article_day_numeric'),

    # do dia atual
    path('archive_day/', ArticleToDay.as_view(month_format='%m'), name='article_today'),

    # detail do dia atual, procurando por pk
    path('archive_pk/<int:year>/<int:month>/<int:day>/<int:pk>/',
         DateDetailView.as_view(month_format='%m', model=Article, date_field="pub_date",
                                template_name='generic_date_view/generic_day_pk.html'), name="archive_date_detail"),
]
