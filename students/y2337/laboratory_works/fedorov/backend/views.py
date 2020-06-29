from datetime import datetime
from decimal import Decimal
from math import ceil

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *


class CarView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            return Response(status=501)
        car = Car.objects.get(pk=pk)
        result = CarSerializer(car, many=False)
        return Response(result.data)


class BeginTrip(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cars = InTripModel.objects.all().values('car').values('pk')
        car = Car.objects.exclude(pk__in=cars).order_by('?').first()
        result = CarSerializer(car, many=False)
        return Response(result.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = Car.objects.get(pk=int(request.data['pk']))
            trip = InTripModel.objects.create(car=car, user=request.user)
            trip.save()
            return Response(200)
        return Response(400)


class EndTrip(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        inTrips = InTripModel.objects.filter(user=request.user)
        for inTrip in inTrips:
            begin = inTrip.begin.replace(tzinfo=None)
            end = datetime.now().replace(tzinfo=None)
            delta = ceil(((end - begin) / 60).total_seconds())
            price = delta * inTrip.car.price
            transaction = Transaction.objects.create(user=request.user, delta=-price)
            trip = Trip.objects.create(car=inTrip.car, transaction=transaction, time=Decimal(delta))
            transaction.save()
            inTrip.delete()
            trip.save()
        return Response('{}', status=200)


class History(APIView):
    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        trips = Trip.objects.filter(transaction__in=transactions)
        result = TripSerializer(trips, many=True)
        return Response(result.data)
