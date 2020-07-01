from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *

from .serializers import *

class Boards(APIView):
  # Доски

  permission_classes = [IsAuthenticated]

  def get(self, request):

    boards = request.user.board.all()

    serializer = BoardSerializers(boards, many=True) # many=True чтобы выбирал и связующие модели
    
    return Response(serializer.data) 

class BoardsDetails(APIView):
  # Панели + каротчки для определенной доски

  permission_classes = [IsAuthenticated]

  def get(self, request, board_id):
    try:
      panels = request.user.board.get(pk=board_id).panel.all()
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 
    
    serializer = PanelSerializers(panels, many=True)

    return Response(serializer.data) 

class CreateBoard(APIView):
  # Создание доски

  permission_classes = [IsAuthenticated]

  def post(self, request):

    try:
      board = Board(title=request.data['title'], user=request.user)
      board.save()
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': 'Доска успешно создана'})

class DeleteBoard(APIView):
  # Удаление доски

  permission_classes = [IsAuthenticated]

  def delete(self, request, board_id):

    try:
      board = request.user.board.get(pk=board_id)
      board.delete()
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST)     

    return Response({'detail': 'Успешно удалено'})

class CreatePanel(APIView):
  # Создание панели

  permission_classes = [IsAuthenticated]

  def post(self, request):

    data = request.data

    try:
      panel = Panel(title=data['title'], index=data['index'], board=request.user.board.get(pk=data['boardId']), user=request.user)
      panel.save()
      serializer = PanelSerializers(panel)
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response(serializer.data)

class DeletePanel(APIView):

  permission_classes = [IsAuthenticated]

  def delete(self, request, panel_id):
    try:
      panel = request.user.panel.get(pk=panel_id)
      panel.delete()

    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 

    return Response({'detail': 'Панель успешно удалена'})

class IndexPanel(APIView):
  # Установка индекса для панели

  permission_classes = [IsAuthenticated]

  def put(self, request):

    try:
      arr = request.data['panels']

      for i in range(len(arr)):
        panel = request.user.panel.get(pk=arr[i]['id'])
        panel.index = arr[i]['index']
        panel.save()

    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response({'detail': 'good'})

class CreateCard(APIView):
  # Добавление карточки

  permission_classes = [IsAuthenticated]

  def post(self, request):

    try:

      data = request.data

      card = Card(value=data['value'], index=data['index'], panel=request.user.panel.get(pk=data['panelId']), user = request.user)

      card.save()

      serializer = CardSerializers(card)
      
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response(serializer.data)


class DeleteCard(APIView):
  # Удаление карточки

  permission_classes = [IsAuthenticated]

  def delete(self, request, card_id):

    try:
      card = request.user.card.get(pk=card_id)
      card.delete()
      
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response({'detail': 'Карточка успешно удалена'})

class IndexCard(APIView):
  # Установка индекса для карточки

  permission_classes = [IsAuthenticated]

  def put(self, request):

    try:
      arr = request.data['cards']
      for i in range(len(arr)):
        card = request.user.card.get(pk=arr[i]['id'])
        card.index = arr[i]['index']
        card.save()

    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response({'detail': 'good'})

class MoveCard(APIView):
  # Перемещение карточек между панелями

  permission_classes = [IsAuthenticated]

  def put(self, request, card_id, panel_id):
    try:
      card = request.user.card.get(pk=card_id)
      panel = request.user.panel.get(pk=panel_id)

      card.panel = panel
      card.save()
    except BaseException:
      return Response({"detail": "Database request error"}, status=status.HTTP_400_BAD_REQUEST) 


    return Response({'detail': 'good'})


