from django.contrib import admin
from django.urls import path

from carevent.views import CarEventListView, remove_table_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('remove_data/', remove_table_data, name='remove_data'),
    path('', CarEventListView.as_view(), name='car_events')
]
