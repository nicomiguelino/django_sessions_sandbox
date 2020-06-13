from django.contrib import messages
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        else:
            request.session.set_test_cookie()
            messages.error(request, 'Please enable cookie')

        return render(request, 'main/index.html')


class SessionReadWriteView(View):
    def get(self, request):
        request.session['user_id'] = 20
        request.session['team'] = 'Barcelona'

        return render(request, 'main/session_read_write_view.html')


class ClearSessionView(View):
    def get(self, request):
        try:
            del request.session['user_id']
            del request.session['team']
        except KeyError:
            pass

        return render(request, 'main/clear_session.html')


class TestCookie01(View):
    def get(self, request):
        request.session.set_test_cookie()
        return render(request, 'main/test_cookie_01.html')


class TestCookie02(View):
    def get(self, request):
        context = {}
        if (request.session.test_cookie_worked()):
            context.update({'cookie_status': 'Test cookie worked!'})
            request.session.delete_test_cookie()

        return render(request, 'main/test_cookie_02.html', context)
