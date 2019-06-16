from django.urls import path
from .views import *

urlpatterns = [
    path('',ProjectsList.as_view(),name='projects_list_url'),
    path('project/<slug>/',ProjectDetail.as_view(),name='project_detail_url')
]
