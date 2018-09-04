from django.shortcuts import render
from django.views.generic import View

import itertools
from collections import OrderedDict
from statistics import mean

from . import utils
from . import questionnaire


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", {})

def data_tourguide(request):
    hvd_tourguide = questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)
    data = hvd_tourguide.questionnaires

    return render(request, "data/tourguide.html",{'data': data})

def data_accommudation(request):
    data = questionnaire.Questionnaires(questionnaire.Accommudation, questionnaire.sheet_url_accommudation).questionnaires

    return render(request, "data/accommudation.html",{'data': data})

def data_cultural(request):
    data = questionnaire.Questionnaires(questionnaire.Cultural, questionnaire.sheet_url_cultural).questionnaires

    return render(request, "data/cultural.html",{'data': data})

def radar_all_data(hvd):
    location_names =[q.location for q in hvd.questionnaires]
    location_names_ordered = list(OrderedDict.fromkeys(location_names))

    labels = ["experience", "exclusive", "expertise", "exceptional", "excellence"]
    data = []
    datasets = []

    for location in location_names_ordered:
        experience_list     = list(itertools.chain(*[filtered_q.get_experience_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exclusive_list      = list(itertools.chain(*[filtered_q.get_exclusive_list() for filtered_q in hvd.filter_by_location_list(location)]))
        expertise_list      = list(itertools.chain(*[filtered_q.get_expertise_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exceptional_list    = list(itertools.chain(*[filtered_q.get_exceptional_list() for filtered_q in hvd.filter_by_location_list(location)]))
        excellence_list     = list(itertools.chain(*[filtered_q.get_excellence_list() for filtered_q in hvd.filter_by_location_list(location)]))

        data.append([location, [
            mean(experience_list),
            mean(exclusive_list),
            mean(expertise_list),
            mean(exceptional_list),
            mean(excellence_list)
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

    data_literacy = questionnaire.json.dumps(data_literacy, sort_keys=True, indent=4)

    return {'data_literacy': data_literacy}

def radar_individual_data(hvd):
    location_names =[q.location for q in hvd.questionnaires]
    location_names_ordered = list(OrderedDict.fromkeys(location_names))

    labels = ["Experience", "Exclusive", "Expertise", "Exceptional", "Excellence"]
    data_literacies = []
    data = []
    canvase_names = []

    for idx, location in enumerate(location_names_ordered):
        dataset = []
        canvase_names.append({'name':"radar-chart-" + str(idx)})

        experience_list     = list(itertools.chain(*[filtered_q.get_experience_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exclusive_list      = list(itertools.chain(*[filtered_q.get_exclusive_list() for filtered_q in hvd.filter_by_location_list(location)]))
        expertise_list      = list(itertools.chain(*[filtered_q.get_expertise_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exceptional_list    = list(itertools.chain(*[filtered_q.get_exceptional_list() for filtered_q in hvd.filter_by_location_list(location)]))
        excellence_list     = list(itertools.chain(*[filtered_q.get_excellence_list() for filtered_q in hvd.filter_by_location_list(location)]))

        dataset = [{
            "label": location,
            "fill": True, 
            "backgroundColor": "rgba(179,181,198,0.2)",
            "borderColor": "rgb(54,162,235)",
            "pointBorderColor": "#fff",
            "pointBackgroundColor": "rgba(179,181,198,1)",
            "data": [
                mean(experience_list),
                mean(exclusive_list),
                mean(expertise_list),
                mean(exceptional_list),
                mean(excellence_list)
                ]
            }]

        data_literacy = questionnaire.json.dumps({"labels": labels, "datasets": dataset}, sort_keys=True, indent=4)
        data_literacies.append(data_literacy)

    return {'canvase_names': canvase_names, 'data': zip(canvase_names, data_literacies)}

def radar_all_tourguide(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_all_accommudation(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.Accommudation, questionnaire.sheet_url_accommudation)))

def radar_all_cultural(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.Cultural, questionnaire.sheet_url_cultural)))

def radar_individual_tourguide(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_individual_accommudation(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.Accommudation, questionnaire.sheet_url_accommudation)))

def radar_individual_cultural(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.Cultural, questionnaire.sheet_url_cultural)))
