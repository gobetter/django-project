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

def get_progress_color(val):
    if val >= 80:
        return "bg-success"
    elif val >= 50:
        return "bg-warning"
    else:
        return "bg-danger"

def radar_individual_data(hvd):
    location_names =[q.location for q in hvd.questionnaires]
    location_names_ordered = list(OrderedDict.fromkeys(location_names))

    labels = ["Experience", "Exclusive", "Expertise", "Exceptional", "Excellence"]
    data_literacies = []
    data = []
    canvase_names = []
    mean_percentage = []
    progress_colors = []

    for idx, location in enumerate(location_names_ordered):
        dataset = []
        canvase_names.append({'name':"radar-chart-" + str(idx)})

        experience_list     = list(itertools.chain(*[filtered_q.get_experience_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exclusive_list      = list(itertools.chain(*[filtered_q.get_exclusive_list() for filtered_q in hvd.filter_by_location_list(location)]))
        expertise_list      = list(itertools.chain(*[filtered_q.get_expertise_list() for filtered_q in hvd.filter_by_location_list(location)]))
        exceptional_list    = list(itertools.chain(*[filtered_q.get_exceptional_list() for filtered_q in hvd.filter_by_location_list(location)]))
        excellence_list     = list(itertools.chain(*[filtered_q.get_excellence_list() for filtered_q in hvd.filter_by_location_list(location)]))

        mean_percentage.append({'value':[
                mean(experience_list)/5*100,
                mean(exclusive_list)/5*100,
                mean(expertise_list)/5*100,
                mean(exceptional_list)/5*100,
                mean(excellence_list)/5*100
                ]})

        progress_colors.append({'color':[
                get_progress_color(mean(experience_list)/5*100),
                get_progress_color(mean(exclusive_list)/5*100),
                get_progress_color(mean(expertise_list)/5*100),
                get_progress_color(mean(exceptional_list)/5*100),
                get_progress_color(mean(excellence_list)/5*100)
                ]})

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

    # return {'canvase_names': canvase_names, 'data': zip(canvase_names, data_literacies)}
    return {'main_data': zip(canvase_names, mean_percentage, progress_colors), 'js_data': zip(canvase_names, data_literacies)}

def radar_all_tourguide(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_all_accommudation(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.Accommudation, questionnaire.sheet_url_accommudation)))

def radar_all_cultural(request):
    return render(request, "radar/radarall.html", radar_all_data(questionnaire.Questionnaires(questionnaire.Cultural, questionnaire.sheet_url_cultural)))


def radar_individual_tourguide(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_individual_natural(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_individual_recreational(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.TourGuide, questionnaire.sheet_url_tourguide)))

def radar_individual_accommudation(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.Accommudation, questionnaire.sheet_url_accommudation)))

def radar_individual_cultural(request):
    return render(request, "radar/radar.html", radar_individual_data(questionnaire.Questionnaires(questionnaire.Cultural, questionnaire.sheet_url_cultural)))


def top_experience(request):
    return render(request, "destinations/topdestinations.html",{'top_name': 'Top Experience', 'prefix': 'experience'})

def top_exclusive(request):
    return render(request, "destinations/topdestinations.html",{'top_name': 'Top Exclusive', 'prefix': 'exclusive'})

def top_expertise(request):
    return render(request, "destinations/topdestinations.html",{'top_name': 'Top Expertise', 'prefix': 'expertise'})

def top_exceptional(request):
    return render(request, "destinations/topdestinations.html",{'top_name': 'Top Exceptional', 'prefix': 'exceptional'})

def top_excellence(request):
    return render(request, "destinations/topdestinations.html",{'top_name': 'Top Excellence', 'prefix': 'excellence'})


def experience_attractions(request):
    return render(request, "destinations/attractions.html",{'attraction_name': 'Experience Attractions'})

def exclusive_attractions(request):
    return render(request, "destinations/attractions.html",{'attraction_name': 'Exclusive Attractions'})

def expertise_attractions(request):
    return render(request, "destinations/attractions.html",{'attraction_name': 'Expertise Attractions'})

def exceptional_attractions(request):
    return render(request, "destinations/attractions.html",{'attraction_name': 'Exceptional Attractions'})

def excellence_attractions(request):
    return render(request, "destinations/attractions.html",{'attraction_name': 'Excellence Attractions'})


def experience_accommudation(request):
    return render(request, "destinations/accommudation.html",{'accommudation_name': 'Experience Accommudation'})

def exclusive_accommudation(request):
    return render(request, "destinations/accommudation.html",{'accommudation_name': 'Exclusive Accommudation'})

def expertise_accommudation(request):
    return render(request, "destinations/accommudation.html",{'accommudation_name': 'Expertise Accommudation'})

def exceptional_accommudation(request):
    return render(request, "destinations/accommudation.html",{'accommudation_name': 'Exceptional Accommudation'})

def excellence_accommudation(request):
    return render(request, "destinations/accommudation.html",{'accommudation_name': 'Excellence Accommudation'})


def experience_tourguide(request):
    return render(request, "destinations/tourguide.html",{'tourguide_name': 'Experience Tour Guide'})

def exclusive_tourguide(request):
    return render(request, "destinations/tourguide.html",{'tourguide_name': 'Exclusive Tour Guide'})

def expertise_tourguide(request):
    return render(request, "destinations/tourguide.html",{'tourguide_name': 'Expertise Tour Guide'})

def exceptional_tourguide(request):
    return render(request, "destinations/tourguide.html",{'tourguide_name': 'Exceptional Tour Guide'})

def excellence_tourguide(request):
    return render(request, "destinations/tourguide.html",{'tourguide_name': 'Excellence Tour Guide'})
