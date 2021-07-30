from django.shortcuts import render
from .models import Quote

from rest_framework import generics, serializers
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly

# Create your views here.

class QuoteListAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    
