from django.urls import path
from .views import (EventListAPIView,EventDetailAPIView,EventUpdateAPIView,EventDeleteAPIView,EventCreateAPIView,
                    VenueListAPIView,VenueDetailAPIView,VenueUpdateAPIView,VenueDeleteAPIView,VenueCreateAPIView)
app_name='event-api'
urlpatterns = [
    path('event/', EventListAPIView.as_view(), name='list'),
    path('event/create/', EventCreateAPIView.as_view(), name='create'),
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='detail'),
    path('event/<int:pk>/update/', EventUpdateAPIView.as_view(), name='update'),
    path('event/<int:pk>/delete/', EventDeleteAPIView.as_view(), name='delete'),
    path('venue/', VenueListAPIView.as_view(), name='venue-list'),
    path('venue/create/', VenueCreateAPIView.as_view(), name='venue-create-api'),
    path('venue/<int:pk>/', VenueDetailAPIView.as_view(), name='venue-detail-api'),
    path('venue/<int:pk>/update/', VenueUpdateAPIView.as_view(), name='venue-update-api'),
    path('venue/<int:pk>/delete/', VenueDeleteAPIView.as_view(), name='venue-delete-api'),
    ]
