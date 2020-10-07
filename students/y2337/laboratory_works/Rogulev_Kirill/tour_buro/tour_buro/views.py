from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework.parsers import JSONParser

from tour_buro.serializers import *

class bus_view(APIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser ]
    def get(self, request):
        buses = Bus.objects.all()

        serializer = BusSerializers(buses, many=True)
        return Response({'data':serializer.data})

    def post(self, request):
        data = JSONParser().parse(request)
        buses = Bus.objects.all()
        serializer = BusSerializers(buses, data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"succ"})
        else:
            return Response({"status":"Err"})

class excursion_route_view(APIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser ]
    def get(self, request):
        Excursion_routes = Excursion_route.objects.all()
        serializer = Excursion_RouteSerializers(Excursion_routes, many=True)
        return Response({'data':serializer.data})

    def post(self, request):
        data = JSONParser().parse(request)
        routes = Excursion_route.objects.all()
        serializer = Excursion_RouteSerializers(routes, data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"succ"})
        else:
            return Response({"status":"Err"})

class crew_member_view(APIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser ]
    def get(self, request):
        crew_members = Crew_member.objects.all()
        serializer = Crew_memberSerializers(crew_members, many=True)
        return Response({'data':serializer.data})

    def post(self, request):
        data = JSONParser().parse(request)
        crew_members = Crew_member.objects.all()
        serializer = Crew_memberSerializers(crew_members, data=data,many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"succ"})
        else:
            return Response({"status":"Err"})

class completed_trip_view(APIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser ]
    def get(self, request):
        Completed_trips = Completed_trip.objects.all()
        serializer = Completed_tripSerializers(Completed_trips, many=True)
        return Response({'data':serializer.data})

    def post(self, request):
        data = JSONParser().parse(request)
        Completed_trips = Completed_trip.objects.all()
        serializer = Completed_tripSerializers(Completed_trips,data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"succ"})
        else:
            return Response({"status":"Err"})

