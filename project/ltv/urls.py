from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("test/", views.test),
    path("api/json", views.test_json),
    path("api/device-os/analysis/", views.device_os_analysis),
    path("api/weekday/analysis/", views.weekday_analysis),
    path("api/device-name/analysis/", views.device_name_analysis),
    path("api/region/analysis/", views.region_analysis),
    path("api/time/analysis/", views.time_analysis),
]
