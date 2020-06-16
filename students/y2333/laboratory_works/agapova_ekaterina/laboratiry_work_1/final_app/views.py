from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from final_app.models import Fabric, Product, Delivery, Sale
from final_app.serializers import UserSerializer, FabricSerializer, ProductSerializer, DeliverySerializer, SaleSerializer, StoreSerializer


User = get_user_model()


@permission_classes([IsAdminUser, ])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@permission_classes([IsAdminUser, ])
class FabricViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer


@permission_classes([IsAdminUser, ])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAdminUser, ])
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


@permission_classes([IsAdminUser, ])
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


def store():
    deliveries = Delivery.objects.all()
    store_result = []
    for delivery in deliveries:
        q_sum = Sale.objects.filter(delivery=delivery.id).aggregate(sum=Coalesce(Sum('quantity'), 0))['sum']
        if delivery.quantity > q_sum:
            store_result.append({
                'id': delivery.id,
                'fabric_name': delivery.product.fabric.name,
                'fabric_country': delivery.product.fabric.country,
                'price_for_sale': delivery.price_for_sale,
                'name': delivery.product.name,
                'vendor_code': delivery.product.vendor_code,
                'quantity': delivery.quantity - q_sum
            })
    return store_result


@permission_classes([AllowAny, ])
class StoreList(APIView):
    serializer_class = StoreSerializer

    def get(self, request):
        data = store()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


@permission_classes([AllowAny, ])
@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    User.objects.create_user(
        serialized.initial_data['username'],
        serialized.initial_data['email'],
        serialized.initial_data['password'],
        date_of_birth=serialized.initial_data['date_of_birth'],
        card=serialized.initial_data['card'],
        first_name=serialized.initial_data['first_name'],
        last_name=serialized.initial_data['last_name'],
    )
    if serialized.is_valid():
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

