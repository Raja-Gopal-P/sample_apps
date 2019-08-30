from django.urls import path
from .views import filter_places, PlaceDetailView

app_name = 'places'

urlpatterns = [
    path('', filter_places, name='places-list'),
    path('<int:id>/', PlaceDetailView.as_view(), name='place-view'),
]
