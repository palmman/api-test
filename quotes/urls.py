from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.QuoteListAPIView.as_view(), name='quotes'),
    path('quote/<int:pk>/', views.QuoteDetailAPIView.as_view(), name='quote_detail'),
]
