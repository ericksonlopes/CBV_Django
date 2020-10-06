from django.views.generic import DetailView, YearArchiveView

from database.models import Article


# detalhes
class DetailViewCBVarticle(DetailView):
    model = Article
    template_name = 'recentes/recentes.html'


# Exibe todos os dados do ano

class ArticleYearView(YearArchiveView):
    queryset = Article.objects.all()

    # Definir campo da database
    date_field = "pub_date"

    # fazer lista de objetos
    make_object_list = True

    # Lançamentos futuros
    allow_future = True
