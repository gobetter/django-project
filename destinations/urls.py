from django.urls import path
from .views import (
        DestinationListView,
        DestinationCreateView,
        DestinationDetailView,
        DestinationUpdateView,
        DestinationDeleteView,
        )

app_name = 'destinations'
urlpatterns = [
    path('',                 DestinationListView.as_view(),   name='destination-list'),
    path('create/',          DestinationCreateView.as_view(), name='destination-create'),
    path('<int:id>/',        DestinationDetailView.as_view(), name='destination-detail'),
    path('<int:id>/update/', DestinationUpdateView.as_view(), name='destination-update'),
    path('<int:id>/delete/', DestinationDeleteView.as_view(), name='destination-delete'),
    ]
