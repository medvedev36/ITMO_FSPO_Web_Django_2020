from django.urls import path
from .views import *

urlpatterns = [
  path('boards', Boards.as_view()),   
  path('board/details/<int:board_id>', BoardsDetails.as_view()),
  path('board/create', CreateBoard.as_view()),
  path('board/delete/<int:board_id>', DeleteBoard.as_view()),
  path('panel/create', CreatePanel.as_view()),
  path('panel/delete/<int:panel_id>', DeletePanel.as_view()),
  path('panel/index', IndexPanel.as_view()),
  path('card/create', CreateCard.as_view()),
  path('card/delete/<int:card_id>', DeleteCard.as_view()),
  path('card/index', IndexCard.as_view()),
  path('card/move/<int:card_id>/<int:panel_id>', MoveCard.as_view()),
]