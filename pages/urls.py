from django.urls import path
from .views import PagesListView, PageView


app_name = 'pages'

urlpatterns = [
    path('', PagesListView.as_view(), name='pages-list'),
    path('<slug:slug>/', PageView.as_view(), name='page-view'),
]