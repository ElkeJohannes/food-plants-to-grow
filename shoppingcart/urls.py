from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('<int:plant_id>/', views.add_to_cart, name='add_to_cart' )
]