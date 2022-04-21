from django.urls import path
from . import views


urlpatterns = [
    path('',views.getItems,name="getItems"),
    path('add/',views.addItem,name="addItem"),
    path('detail/<str:pk>/',views.singleItem,name="single-item"),
    path('update/<str:pk>/',views.updateItem,name="update-item"),
    path('delete/<str:pk>/',views.deleteItem,name="delete-item"),
]


 