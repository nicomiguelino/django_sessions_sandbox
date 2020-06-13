from django.urls import path

from site_counter.views import IndexView


app_name = 'site_counter'
urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
