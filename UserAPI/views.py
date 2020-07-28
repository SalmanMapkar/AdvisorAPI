from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserModel
from .serializers import UserDataSerializer, UserReturnSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import jwt
import json

class UserDataRegistration(APIView):
    def get(self,request):
        data=UserModel.objects.all()
        serializer=UserDataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data=UserModel.objects.get(Email=request.data["Email"])
        serializer=UserReturnSerializer(data)
        token = jwt.encode({'Email': str(request.data['Email']), 'Password': str(request.data['Password'])}, 'secret', algorithm='HS256')
        fdata={"Token": token.decode("utf-8"), "UserId": serializer.data['UserId']}
        return Response(fdata, status=status.HTTP_200_OK)

class UserDataView(APIView):
    def post(self, request):
        if request.data["Email"] is "":
            return Response({"Empty email field"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["Password"] is "":
            return Response({"Empty password field"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                data = UserModel.objects.get(Email=request.data["Email"])
            except:
                return Response({"Check your email. No such user"}, status=status.HTTP_401_UNAUTHORIZED)
            serializer = UserReturnSerializer(data)
            if serializer.data["Password"] != request.data["Password"]:
                return Response({"Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)
            token = jwt.encode({'Email': str(request.data['Email']), 'Password': str(request.data['Password'])},
                               'secret', algorithm='HS256')
            fdata = {"Token": token.decode("utf-8"), "UserId": serializer.data['UserId']}
            return Response(fdata, status=status.HTTP_200_OK)

