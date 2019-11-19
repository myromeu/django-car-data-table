from django.contrib import admin
from django.urls import path

from tutorial.views import PersonListView, CarEventListView, remove_table_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path("people/", PersonListView.as_view()),
    path("remove_data/", remove_table_data, name='remove_data'),
    path("carevents/", CarEventListView.as_view(), name='car_events')
]
