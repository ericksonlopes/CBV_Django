from django.views.generic import DetailView, YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, \
    TodayArchiveView

from database.models import Article


# detalhes
class DetailViewCBVarticle(DetailView):
    model = Article
    template_name = 'generic_date_view/generic_date_view.html'


# Exibe todos os dados do ano
class ArticleYearView(YearArchiveView):
    queryset = Article.objects.all()

    # Definir campo da database
    date_field = "pub_date"

    # fazer lista de objetos
    make_object_list = True

    # Lançamentos futuros
    allow_future = True

    template_name = 'generic_date_view/por_ano.html'


# Exibe todos os dados do mes ano/mes
class ArticleMonthView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_date'
    allow_future = True
    template_name = 'generic_date_view/por_mes_ano.html'


# Exibe todos os dados do semana ano/mes/week
class ArticleWeekView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_date'
    allow_future = True
    template_name = 'generic_date_view/por_semana.html'


# Exibir todos os dados do dia ano/mes/dia
class ArticleDayView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_date'
    allow_future = True
    template_name = 'generic_date_view/por_dia.html'


# Do dia atual
class ArticleToDay(TodayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
    template_name = 'generic_date_view/por_dia_atual.html'
