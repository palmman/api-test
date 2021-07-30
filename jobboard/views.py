from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import JobOffer
from .serializers import JobOfferSerializer


class JobOfferList(APIView):

    def get(self, request):
        try:
            jobs = JobOffer.objects.all()
            serializer = JobOfferSerializer(jobs, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobOfferDetail(APIView):

    def get(self, request, pk):
        job = JobOffer.objects.get(pk=pk)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk):
        job = JobOffer.objects.get(pk=pk)
        serializer = JobOfferSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job = JobOffer.objects.get(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# Create your views here.
