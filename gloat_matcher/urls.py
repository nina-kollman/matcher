from django.urls import path
from matcher.views import search_job, search_partial


urlpatterns = [
    path('job/', search_job),
    path('partial/', search_partial)
]
