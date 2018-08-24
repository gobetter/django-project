# import json
# import ast

from django.http import JsonResponse
# from urllib.request import urlopen

# from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic import View

# from .utils import google_sheets_json_to_dict
from . import utils
from . import gsheets

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", {})

def json(request):
    # # data = google_sheets_json_to_dict('1VgFNXoWlQ_ad3CanDioWcqwRzEJLZVPBOS-eCBZ42gg')
    # data = google_sheets_json_to_dict('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')

    # data = utils.gsheets_worksheets('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')

    hvd_tourguide = gsheets.WorkSheet('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')
    data = hvd_tourguide.sheet[0].questionnaire

    # filtered = list(gsheets.filter_by_location(hvd_tourguide.sheet[0].questionnaire, 'เกาะรอก'))
    # data = filtered

    return render(request, "data.html",{'data': data})
    # return JsonResponse(data)
    # return JsonResponse(simple_data, safe=False)
