from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        context_dict = {}

        visits = int(request.COOKIES.get('visits', '1'))
        reset_last_visit_time = False

        if 'last_visit' in request.COOKIES:
            last_visit = request.COOKIES['last_visit']
            last_visit_time = datetime.strptime(
                last_visit[:-7], "%Y-%m-%d %H:%M:%S")

            if (datetime.now() - last_visit_time).days > 0:
                visits = visits + 1
                reset_last_visit_time = True
        else:
            reset_last_visit_time = True
            context_dict['visits'] = visits

        response = render(request, 'site_counter/index.html', context_dict)

        if reset_last_visit_time:
            response.set_cookie('last_visit', datetime.now())
            response.set_cookie('visits', visits)

        return response
