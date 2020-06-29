from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.

from autoApp.serializers import *
from autoApp.models import *

class Autoshop(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        shops = Autoshops.objects.all()
        serializer = Autoshops_Serializers(shops, many=True)
        return Response({"data": serializer.data})

class Master(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        masters = Masters.objects.all()
        serializer = Masters_Serializers(masters, many=True)
        return Response({"data": serializer.data})

class Custumers(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        custumer = Costumer.objects.all()
        serializer = Custumer_Serializers(custumer, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = Custumer_Serializers(data=request.data)
        if client.is_valid():
            client.save()
            return Response({"status":"Add"})
        else:
            return Response({"status":"Error"})

class Car(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        car = Cars.objects.all()
        serializer = Cars_Serializers(car, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        car = Cars_Post_Serializers(data=request.data)
        if car.is_valid():
            car.save()
            return Response({"status":car.data})
        else:
            return Response({"status":car.data})

class Works(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        work = Completed_Works.objects.all()
        serializer = Works_Serializers(work, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        work = Works_Post_Serializers(data=request.data)
        if work.is_valid():
            work.save()
            return Response({"status":work.data})
        else:
            return Response({"status":work.data})

    def put(self, request, pk):
        saved_work = get_object_or_404(Completed_Works.objects.all(), pk=pk)
        serializer = Works_Post_Serializers(instance=saved_work, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            work_saved = serializer.save()
            return Response(status = 201)
        else:
            return Response(status=400)

class ComWorks(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        work = Comprehensive_Repair.objects.all()
        serializer = Comrepair_Post_Serializers(work, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        work = Comrepair_Post_Serializers(data=request.data)
        if work.is_valid():
            work.save()
            return Response({"status": work.data})
        else:
            return Response({"status": work.data})

class Model(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        model = Car_Models.objects.all()
        serializer = Models_Serializers(model, many=True)
        return Response({"data": serializer.data})
