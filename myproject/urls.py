from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pages.views import (
        HomeView,
        data_tourguide, data_accommudation, data_cultural,
        radar_individual_tourguide, radar_individual_accommudation, radar_individual_cultural,
        radar_all_tourguide, radar_all_accommudation, radar_all_cultural
        )
from pages import questionnaire

urlpatterns = [
        path('data_tourguide/', data_tourguide, name='data_tourguide'),
        path('data_accommudation/', data_accommudation, name='data_accommudation'),
        path('data_cultural/', data_cultural, name='data_cultural'),

        path('radar_individual_tourguide/', radar_individual_tourguide, name='radar_individual_tourguide'),
        path('radar_individual_accommudation/', radar_individual_accommudation, name='radar_individual_accommudation'),
        path('radar_individual_cultural/', radar_individual_cultural, name='radar_individual_cultural'),

        path('radar_all_tourguide/', radar_all_tourguide, name='radar_all_tourguide'),
        path('radar_all_accommudation/', radar_all_accommudation, name='radar_all_accommudation'),
        path('radar_all_cultural/', radar_all_cultural, name='radar_all_cultural'),

        path('', HomeView.as_view(), name='home'),
        path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
        path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

        path('admin/', admin.site.urls),
        ]
