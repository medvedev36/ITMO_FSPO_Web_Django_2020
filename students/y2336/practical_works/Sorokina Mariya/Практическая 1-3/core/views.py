from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *

from .serializers import *

class Attractions(APIView):

  def get(self, request, attraction_id):
    attraction = Attraction.objects.get(pk=attraction_id)

    serializer = AttractionSerializers(attraction)

    return Response(serializer.data)

class UseAttractions(APIView):

  def get(self, request):
    use_attraction = Use_attraction.objects.all()

    serializer = UseAttractionSerializers(use_attraction, many=True)

    return Response(serializer.data)

class Playgrounds(APIView):

  def get(self, request):
    playgrounds = Playground.objects.all()

    serializer = PlaygroundSerializers(playgrounds, many=True)

    return Response(serializer.data)

class PopularAttraction(APIView):

  def get(self, request):
    use_attraction = Use_attraction.objects.order_by('-adult_ticket','-children_ticket')[0:1]

    serializer = UseAttractionSerializers(use_attraction, many=True)

    return Response(serializer.data)

class Purchase(APIView):

  permission_classes = [IsAuthenticated]

  def get(self, request):
    my_purchase = request.user.my_purchase.all()

    serializer = MyPurchaseSerializers(my_purchase, many=True)

    return Response(serializer.data)


class BuyTicket(APIView):

  permission_classes = [IsAuthenticated]

  def post(self, request, attraction_id):
    
    try:
      attraction = Attraction.objects.get(pk=attraction_id)
      use_attraction = Use_attraction.objects.get(attraction=attraction)

      if (request.data['type'] == "adult"):
        price = attraction.adult_price
        use_attraction.adult_ticket += 1
        use_attraction.save()
      else:
        price = attraction.children_price
        use_attraction.children_ticket += 1
        use_attraction.save()

      my_purchase = My_purchase(price=price, user=request.user, attraction=attraction)
      my_purchase.save()
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST)

    return Response('Покупка совершена')

class Types(APIView):

  def get(self, request):

    types = AttractionType.objects.all()

    serializer = AttractionTypeSerializers(types, many=True)

    return Response(serializer.data)

