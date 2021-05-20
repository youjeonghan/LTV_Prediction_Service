from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("api/json/", views.test_json),
    path("api/prediction/", views.income_predict),
    path("api/device-os/analysis/", views.device_os_analysis),
    path("api/weekday/analysis/", views.weekday_analysis),
    path("api/device-name/analysis/", views.device_name_analysis),
    path("api/region/analysis/", views.region_analysis),
    path("api/time/analysis/", views.time_analysis),
]
