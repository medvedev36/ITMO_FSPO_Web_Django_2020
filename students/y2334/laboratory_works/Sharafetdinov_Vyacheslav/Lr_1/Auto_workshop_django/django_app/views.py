from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .serializers import *


@api_view(['GET'])
@permission_classes([AllowAny])
def Workshops_list(request):
    workshop_objects = Workshop.objects.all()
    serialized = Workshops_serial(workshop_objects, many=True)
    return Response({'data': serialized.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Onwer_autos_list(request):
    user = request.user
    try:
        autos = Auto.objects.filter(owner=user)
    except Auto.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serialized = Autos_for_owner_serial(autos, many=True)
    return Response({'data': serialized.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Owner_auto_add(request):
    new_auto = Autos_for_owner_serial(data=request.data)
    if new_auto.is_valid():
        new_auto.save(owner=request.user)
        return Response(new_auto.data)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Owner_auto_edit(request, pk):
    try:
        old_auto = Auto.objects.get(id=pk)
    except Auto.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serialized = Autos_for_owner_serial(instance=old_auto, data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Owner_auto_remove(request, pk):
    try:
        auto = Auto.objects.get(id=pk)
    except Auto.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    auto.delete()
    return Response(request.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def Owner_registration(request):
    new_owner = Owner_registration_serial(data=request.data)
    if new_owner.is_valid():
        new_owner.save()
        return Response(new_owner.data)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Owner_applications_list(request):
    try:
        applications = Application.objects.filter(auto__in=(Auto.objects.filter(owner=request.user)))
    except Application.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    for application in applications:
        application.date = application.date.strftime('%Y-%m-%d')
        application.date_init = application.date_init.strftime('%Y-%m-%d %H:%M:%S')
        application.status = application.get_status_display()
    serialized = Applications_for_owner_serial(applications, many=True)
    return Response({'data': serialized.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Workshops_for_application_list(request):
    workshop_objects = Workshop.objects.all()
    serialized = Workshops_for_application_serial(workshop_objects, many=True)
    return Response({'data': serialized.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Owner_application_add(request):
    new_application = Application_serial(data=request.data)
    print(new_application)
    if new_application.is_valid():
        new_application.save()
        return Response(new_application.data)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Owner_application_remove(request, pk):
    try:
        application = Application.objects.get(id=pk)
    except Application.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    application.delete()
    return Response(request.data, status=status.HTTP_200_OK)