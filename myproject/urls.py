from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pages.views import (
        HomeView,
        data_tourguide, data_accommudation, data_cultural,
        radar_individual_tourguide, radar_individual_natural, radar_individual_recreational, radar_individual_accommudation, radar_individual_cultural,
        radar_all_tourguide, radar_all_accommudation, radar_all_cultural,
        top_experience, top_exclusive, top_expertise, top_exceptional, top_excellence,
        experience_attractions, exclusive_attractions, expertise_attractions, exceptional_attractions, excellence_attractions,
        experience_accommudation, exclusive_accommudation, expertise_accommudation, exceptional_accommudation, excellence_accommudation,
        experience_tourguide, exclusive_tourguide, expertise_tourguide, exceptional_tourguide, excellence_tourguide,
        )
from pages import questionnaire

urlpatterns = [
        path('data_tourguide/',     data_tourguide,     name='data_tourguide'),
        path('data_accommudation/', data_accommudation, name='data_accommudation'),
        path('data_cultural/',      data_cultural,      name='data_cultural'),

        path('radar_individual_tourguide/',     radar_individual_tourguide,     name='radar_individual_tourguide'),
        path('radar_individual_natural/',       radar_individual_natural,       name='radar_individual_natural'),
        path('radar_individual_recreational/',  radar_individual_recreational,  name='radar_individual_recreational'),
        path('radar_individual_accommudation/', radar_individual_accommudation, name='radar_individual_accommudation'),
        path('radar_individual_cultural/',      radar_individual_cultural,      name='radar_individual_cultural'),

        path('radar_all_tourguide/',     radar_all_tourguide,     name='radar_all_tourguide'),
        path('radar_all_accommudation/', radar_all_accommudation, name='radar_all_accommudation'),
        path('radar_all_cultural/',      radar_all_cultural,      name='radar_all_cultural'),

        path('top_experience/',  top_experience,  name='top_experience'),
        path('top_exclusive/',   top_exclusive,   name='top_exclusive'),
        path('top_expertise/',   top_expertise,   name='top_expertise'),
        path('top_exceptional/', top_exceptional, name='top_exceptional'),
        path('top_excellence/',  top_excellence,  name='top_excellence'),

        path('experience_attractions/',  experience_attractions,  name='experience_attractions'),
        path('exclusive_attractions/',   exclusive_attractions,   name='exclusive_attractions'),
        path('expertise_attractions/',   expertise_attractions,   name='expertise_attractions'),
        path('exceptional_attractions/', exceptional_attractions, name='exceptional_attractions'),
        path('excellence_attractions/',  excellence_attractions,  name='excellence_attractions'),

        path('experience_accommudation/',  experience_accommudation,  name='experience_accommudation'),
        path('exclusive_accommudation/',   exclusive_accommudation,   name='exclusive_accommudation'),
        path('expertise_accommudation/',   expertise_accommudation,   name='expertise_accommudation'),
        path('exceptional_accommudation/', exceptional_accommudation, name='exceptional_accommudation'),
        path('excellence_accommudation/',  excellence_accommudation,  name='excellence_accommudation'),

        path('experience_tourguide/',  experience_tourguide,  name='experience_tourguide'),
        path('exclusive_tourguide/',   exclusive_tourguide,   name='exclusive_tourguide'),
        path('expertise_tourguide/',   expertise_tourguide,   name='expertise_tourguide'),
        path('exceptional_tourguide/', exceptional_tourguide, name='exceptional_tourguide'),
        path('excellence_tourguide/',  excellence_tourguide,  name='excellence_tourguide'),

        path('', HomeView.as_view(), name='home'),
        path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
        path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

        path('admin/', admin.site.urls),

        path('destinations/', include('destinations.urls')),
        ]
