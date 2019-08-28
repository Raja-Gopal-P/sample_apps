from django.urls import path
from .views import PagesListView


app_name = 'pages'

urlpatterns = [
    path('', PagesListView.as_view(), name='pages-list'),
]