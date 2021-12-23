"""
    Define URLs for the API.

"""

from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import EventViewSet, SensorViewSet

# Create the router
router = routers.DefaultRouter()
router.register('events', EventViewSet)
router.register('sensors',SensorViewSet)

# ADD the routes to the viewsets.

# Here the patterns to expose.
urlpatterns = [
    path('', include(router.urls))
]
