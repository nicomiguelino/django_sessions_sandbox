from django.urls import path

from main.views import (
    IndexView, SessionReadWriteView, ClearSessionView, TestCookie01,
    TestCookie02
)


app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('session_read_write/', SessionReadWriteView.as_view(), name='session_read_write'),
    path('clear_session/', ClearSessionView.as_view(), name='clear_session'),

    path('test_cookie_01/', TestCookie01.as_view(), name='test_cookie_01'),
    path('test_cookie_02/', TestCookie02.as_view(), name='test_cookie_02')
]
