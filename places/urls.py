from django.urls import path
from .views import PlacesListView

app_name = 'places'

urlpatterns = [
    path('', PlacesListView.as_view(), name='places-list'),
]
