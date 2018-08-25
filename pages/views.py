# import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from collections import OrderedDict
from statistics import mean

from . import utils
from . import gsheets

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", {})

def json(request):
    hvd_tourguide = gsheets.WorkSheet('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')
    data = hvd_tourguide.sheet[0].questionnaire

    # data = hvd_tourguide.sheet[0].get_experience_list()

    # filtered = gsheets.hvd_tourguide.sheet[0].filter_by_location_list('สระมรกต')
    # data = filtered

    return render(request, "data.html",{'data': data})
    # return JsonResponse(data)
    # return JsonResponse(simple_data, safe=False)

def radar(request):
    hvd_tourguide = gsheets.WorkSheet('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')

    location_names =[item.ans_location for item in hvd_tourguide.sheet[0].questionnaire]
    location_names_ordered = list(OrderedDict.fromkeys(location_names))

    labels = ["Experience", "Exclusive", "Expertise", "Exceptional", "Excellence"]
    data = []
    datasets = []

    for location in location_names_ordered:
        filtered = hvd_tourguide.sheet[0].filter_by_location_list(location)

        data.append([location, [
            mean(gsheets.get_experience_list(filtered)),
            mean(gsheets.get_exclusive_list(filtered)),
            mean(gsheets.get_expertise_list(filtered)),
            mean(gsheets.get_exceptional_list(filtered)),
            mean(gsheets.get_excellence_list(filtered))
            ]])

    for d in data:
        datasets.append({
            "label": d[0], 
            "fill": True, 
            "backgroundColor": "rgba(179,181,198,0.2)",
            "borderColor": "rgb(54,162,235)",
            "pointBorderColor": "#fff",
            "pointBackgroundColor": "rgba(179,181,198,1)",
            "data": d[1]
            })

    data_literacy = {"labels": labels, "datasets": datasets}

    data_literacy = gsheets.json.dumps(data_literacy, sort_keys=True, indent=4)
    # print(gsheets.json.dumps(data_literacy, sort_keys=True, indent=4))

    return render(request, "radar.html", {'data_literacy': data_literacy})
    # return JsonResponse(data)
    # return JsonResponse(simple_data, safe=False)
