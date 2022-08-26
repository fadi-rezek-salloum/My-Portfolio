from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('project-details/<slug>/', views.ProjectDetails.as_view(), name='details'),
]
