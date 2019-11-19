from django.contrib import admin
from django.urls import path

from tutorial.views import PersonListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("people/", PersonListView.as_view()),
]
