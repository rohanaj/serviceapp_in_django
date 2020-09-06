from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,GenericAPIView
from rest_framework.views import APIView
from .models import State,RequestType,Status

from .serializers import *


class StateView(APIView):

    def get(self,request):
        states = State.objects.all()
        serializer = StateSerializer(states,many=True)
        return Response(serializer.data)
    def post(self,request):

        serializer = StateSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            state_saved = serializer.save()
        return Response({"success": "Country '{}' created successfully".format(state_saved.state)})

class RequestTypeView(APIView):
    def get(self,request):
        requesttype = RequestType.objects.all()
        serializer = RequestTypeSerializer(requesttype,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = RequestTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            type_saved = serializer.save()
        return Response({"success": "Request Type '{}'  created successfully".format(type_saved.requesttype)})


class StatusView(APIView):
    def get(self,request):
        status = Status.objects.all()
        serializer = StatusSerializer(status,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StatusSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            status_saved = serializer.save()
        return Response({"success":"Status '{}'  created successfully".format(status_saved.status)})


class NewRequestView(CreateAPIView):
    serializer_class = NewRequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = RequestList.objects.all()
    def get(self,request):
        newreq = RequestList.objects.all()
        serializer = NewRequestSerializer(newreq,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        #requesttypeserializer = RequestTypeSerializer(data.get(""))
        serializer = NewRequestSerializer(data = request.data)
        #for k,v in data.items():
        #    if isinstance(v, list):  # <- is the main logic
        #        serializer = RequestTypeSerializer(data=request.data[k], many=True,read_only=True)
        #        print(serializer)
        #    else:
        #        serializer = self.get_serializer(data=request.data[k])
        #        print(serializer)
        #if serializer.is_valid():
        #    serializer.save()
        #if serializer.is_valid(raise_exception=True):
        #    newreq_saved = serializer.save()
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
        return Response({"success":"Request list created successfully"})


        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateRequestView(RetrieveUpdateAPIView):
    serializer_class = UpdateRequestSerializer
    queryset = RequestList.objects.all()
    permission_classes = [IsAuthenticated,IsAdminUser]
    def put(self,request,pk):
        requestlist = get_object_or_404(RequestList,pk=pk)
        data = request.data
        print(data)
        serializer = UpdateRequestSerializer(instance=requestlist,data=data,partial=True)
        if serializer.is_valid(raise_exception=True):
            savedlist = serializer.save()
        return Response("Request list with id = {} updated successfully".format(savedlist.pk))



