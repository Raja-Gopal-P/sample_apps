from django.views.generic import ListView, DetailView

from .models import Director


class DirectorListView(ListView):
    model = Director
    context_object_name = 'directors'
    template_name = 'movies/director-list.html'


class DirectorDetailView(DetailView):
    model = Director
    pk_url_kwarg = 'id'
    context_object_name = 'director'
    template_name = 'movies/director-detail-view.html'
