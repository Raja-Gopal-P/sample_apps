from django.urls import path
from .views import PlacesListView, PlaceDetailView

app_name = 'places'

urlpatterns = [
    path('', PlacesListView.as_view(), name='places-list'),
    path('<int:id>/', PlaceDetailView.as_view(), name='place-view'),
]
