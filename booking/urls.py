from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check, name="check"),
    path('check/<int:id>/', views.check, name="check"),
    path('detalles-reserva/<str:opc>/', views.det_booking, name="detail_booking"),
]