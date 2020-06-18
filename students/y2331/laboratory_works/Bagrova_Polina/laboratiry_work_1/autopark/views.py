from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from autopark.serializers import *


class DriversView(APIView):
    """Водители"""

    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        drivers = Drivers.objects.all()
        serializer = DriversSerializer(drivers, many=True)
        return Response({"data": serializer.data})


class CarsView(APIView):
    """Машины"""

    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response({"data": serializer.data})


class ClientsView(APIView):
    """Клиенты"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        clients = Clients.objects.all()
        if pk is not None:
            clients = Clients.objects.filter(pk=pk)
        serializer = ClientsSerializer(clients, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = ClientsSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_client = get_object_or_404(Clients.objects.all(), pk=pk)
        data = request.data
        serializer = ClientsSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        client = get_object_or_404(Clients.objects.all(), pk=pk)
        client.delete()
        return Response(status=204)


class ManifestsView(APIView):
    """Путевой лист и номера заказов для него"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        if pk is not None:
            manifest = Manifests.objects.filter(pk=pk)
            serializerManifest = ManifestsSerializer(manifest, many=True)
            order = Orders.objects.filter(manifest_id=pk)
            serializerOrder = OrdersSerializer(order, many=True)
            return Response({"manifest": serializerManifest.data, "orders": serializerOrder.data})
        manifests = Manifests.objects.all()
        serializerManifest = ManifestsSerializer(manifests, many=True)
        return Response({"manifest": serializerManifest.data})

    def post(self, request):
        id = User.objects.values_list('id', flat=True).get(username=request.user)
        driver = Drivers.objects.values_list('id', flat=True).get(user=id)
        manifest = ManifestsPostSerializer(data=request.data)
        if manifest.is_valid():
            manifest.save(driver_id=driver)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_manifest = get_object_or_404(Manifests.objects.all(), pk=pk)
        data = request.data
        serializer = ManifestsSerializer(instance=saved_manifest, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        manifest = get_object_or_404(Manifests.objects.all(), pk=pk)
        manifest.delete()
        return Response(status=204)


class OrdersView(APIView):
    """Заказы и их состав"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        orders = Orders.objects.all()
        if pk is not None:
            orders = Orders.objects.filter(pk=pk)
            serializerOrder = OrdersSerializer(orders, many=True)
            client = Clients.objects.filter(id=Orders.objects.values_list('client', flat=True).get(pk=pk))
            serializerClient = ClientsSerializer(client, many=True)
            composition = Order_composition.objects.filter(order_id=pk)
            serializerComposition = OrderCompositionSerializer(composition, many=True)
            return Response(
                {"orders": serializerOrder.data, "items": serializerComposition.data, "client": serializerClient.data})
        serializerOrder = OrdersSerializer(orders, many=True)
        return Response({"orders": serializerOrder.data})

    def post(self, request):
        order = OrdersSerializer(data=request.data)
        if order.is_valid():
            order.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_order = get_object_or_404(Orders.objects.all(), pk=pk)
        data = request.data
        serializer = OrdersSerializer(instance=saved_order, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        order = get_object_or_404(Orders.objects.all(), pk=pk)
        order.delete()
        return Response(status=204)
