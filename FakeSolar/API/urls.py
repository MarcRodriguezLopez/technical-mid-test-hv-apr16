from django.urls import path

from . import views

urlpatterns = [
    path('solargrade/inspections', views.inspecions_list, name='index'),
]