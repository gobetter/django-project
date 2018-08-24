from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from pages.views import HomeView, json

urlpatterns = [
        path('data/', json, name='data'),

        path('', HomeView.as_view(), name='home'),
        path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
        path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

        path('admin/', admin.site.urls),
        ]
