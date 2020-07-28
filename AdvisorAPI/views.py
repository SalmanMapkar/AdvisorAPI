from django.shortcuts import render
from rest_framework.views import APIView
from .models import AdvisorDataModel, AdvisorBookingModel
from .serializers import AdvisorDataSerializer, AdvisorlistSerializer, AdvisorBookingSerializer, AllBookedAdvisorSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import jwt
import json
from django.core import serializers

class AdminAdvisorView(APIView):
    def get(self,request):
        data=AdvisorDataModel.objects.all()
        serializer=AdvisorDataSerializer(data, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer=AdvisorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllAdvisorView(APIView):
    def get(self, request, UserId):
        advisordata=AdvisorDataModel.objects.all()
        serializer=AdvisorlistSerializer(advisordata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookAdvisorView(APIView):
    def post(self, request, UserId, AdvisorId):
        serializer = AdvisorBookingSerializer(data={"UserId": UserId, "AdvisorId": AdvisorId, 'BookingTime': request.data['BookingTime']})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllBookedAdvisor(APIView):
    def get(self, request, UserId, AdvisorId):
        advisordata = AdvisorBookingModel.objects.filter(UserId=UserId)
        serializer = AllBookedAdvisorSerializer(advisordata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)