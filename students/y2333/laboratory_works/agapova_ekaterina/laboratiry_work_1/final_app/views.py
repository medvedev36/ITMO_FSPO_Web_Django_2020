from datetime import date

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from final_app.models import Fabric, Product, Delivery, Sale
from final_app.serializers import UserSerializer, FabricSerializer, ProductSerializer, DeliverySerializer, \
    SaleSerializer, StoreSerializer, UserSalesSerializer

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
                'quantity': delivery.quantity - q_sum,
                'image': delivery.product.image,
            })
    return store_result


@permission_classes([AllowAny, ])
class StoreList(APIView):
    serializer_class = StoreSerializer

    def get(self, request):
        data = store()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
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


@permission_classes([IsAuthenticated, ])
class OwnUserViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


@permission_classes([IsAuthenticated, ])
class UserData(APIView):
    def get(self, request):
        user_data = {
            'date_of_birth': request.user.date_of_birth,
            'card': request.user.card,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'is_superuser': request.user.is_superuser,
        }
        serialized = UserSerializer(data=user_data)
        if serialized.is_valid():
            return Response(serialized.data)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = request.user
            user.email = serialized.data['email']
            user.date_of_birth = serialized.data['date_of_birth']
            user.card = serialized.data['card']
            user.first_name = serialized.data['first_name']
            user.last_name = serialized.data['last_name']
            user.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


def user_sales(user):
    sales = Sale.objects.filter(user=user).all()
    sales_result = []
    for sale in sales:
        sales_result.append({
            'id': sale.id,
            'quantity': sale.quantity,
            'name': sale.delivery.product.name,
            'total': sale.quantity * sale.delivery.price_for_sale,
            'date': sale.date
        })
    return sales_result


@permission_classes([IsAuthenticated, ])
class UserSales(APIView):
    def post(self, request):
        sale = {
            'user': request.user,
            'quantity': request.data['quantity'],
            'delivery': Delivery.objects.get(pk=request.data['id']),
            'date': date.today()
        }
        new_sale = Sale(**sale)
        new_sale.save()
        return Response('OK', status=status.HTTP_201_CREATED)

    def get(self, request):
        sales = user_sales(request.user)
        serialized = UserSalesSerializer(data=sales, many=True)
        if serialized.is_valid():
            return Response(serialized.data)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)