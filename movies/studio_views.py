from django.views.generic import ListView, DetailView

from .models import Studio


class StudioListView(ListView):
    model = Studio
    context_object_name = 'studios'
    template_name = 'movies/studio-list.html'


class StudioDetailView(DetailView):
    model = Studio
    slug_url_kwarg = 'slug'
    context_object_name = 'studio'
    template_name = 'movies/studio-detail-view.html'
