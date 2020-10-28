from django.urls import path
from .views import *

urlpatterns = [
    path('addDisk/', addDisk, name="add_disk-url"),
    path('addAuthor/', addAuthor, name="add_author-url"),
    path('addMusic/', addMusic, name="add_music-url"),
    path('', disk_list, name="disk_list-url"),
    path('addProducer/', addProducer, name="add_producer-url"),
    path('editCost/<int:id>/', editCost),
    path('delete/<int:id>/', delete),
    path('editMusic/<int:id>', editMusic),
    path('editPro/<int:id>', editPro),
    path('editAuthor/<int:id>', editAuthor),
]