from django.urls import path
from main.views import (
    IndexView, SessionReadWriteView, ClearSessionView)

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('session_read_write/', SessionReadWriteView.as_view(), name='session_read_write'),
    path('clear_session/', ClearSessionView.as_view(), name='clear_session')
]
