from django.urls import path
from .views import EventDateFilterRedirect, filter_by_date, filter_by_month, filter_by_year, \
    EventDetailView, create_event_view, add_event_timing_view


app_name = 'events'

urlpatterns = [
    path('', EventDateFilterRedirect.as_view(), name='events-list'),
    path('filter-by-date/', filter_by_date, name='events-list-date-filter'),
    path('filter-by-month/', filter_by_month, name='events-list-month-filter'),
    path('filter-by-year/', filter_by_year, name='events-list-year-filter'),
    path('<int:id>/', EventDetailView.as_view(), name='event-view'),
    path('create/', create_event_view, name="create-event"),
    path('<int:event_id>/timing/add', add_event_timing_view, name="add-event-timing"),
]