from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        context_dict = {}

        visits = request.session.get('visits', 1)
        reset_last_visit_time = False

        last_visit = request.session.get('last_visit')
        if last_visit:
            last_visit_time = datetime.strptime(
                last_visit[:-7], "%Y-%m-%d %H:%M:%S")

            if (datetime.now() - last_visit_time).seconds > 0:
                visits = visits + 1
                reset_last_visit_time = True
        else:
            reset_last_visit_time = True

        if reset_last_visit_time:
            request.session['last_visit'] = str(datetime.now())
            request.session['visits'] = visits

        context_dict['visits'] = visits

        response = render(request, 'site_counter/index.html', context_dict)

        return response
