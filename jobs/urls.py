from django.urls import path
from . import views

urlpatterns = [
    path('fetch-jobs/', views.fetch_jobs, name='fetch_jobs'),
    path('table/', views.table_view, name='table_view'),
    path('map/', views.map_view, name='map_view'),
]