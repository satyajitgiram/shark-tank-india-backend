# myapp/urls.py

from django.urls import path
from .views import (
    EntrepreneurListCreateView,
    EntrepreneurRetrieveUpdateDestroyView,
    PitchListCreateView,
    PitchRetrieveUpdateDestroyView,
    SharkListCreateView,
    SharkRetrieveUpdateDestroyView,
    ContactListCreateView,
    ContactRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('entrepreneurs/', EntrepreneurListCreateView.as_view(), name='entrepreneurs-list'),
    path('entrepreneurs/<int:pk>/', EntrepreneurRetrieveUpdateDestroyView.as_view(), name='entrepreneurs-detail'),
    path('pitches/', PitchListCreateView.as_view(), name='pitches-list'),
    path('pitches/<int:pk>/', PitchRetrieveUpdateDestroyView.as_view(), name='pitches-detail'),
    path('sharks/', SharkListCreateView.as_view(), name='sharks-list'),
    path('sharks/<int:pk>/', SharkRetrieveUpdateDestroyView.as_view(), name='sharks-detail'),
    path('contact-us/', ContactListCreateView.as_view(), name='contact-list'),
    path('contact-us/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),
]


# 9993869873