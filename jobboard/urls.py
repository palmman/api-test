from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobOfferList.as_view(), name='jobslist'),
    path('jobs/<int:pk>/', views.JobOfferDetail.as_view(), name='job_detail'),
]
