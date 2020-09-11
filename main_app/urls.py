from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orchids/', views.orchids_index, name='index'),
    path('orchids/<int:orchid_id>/', views.orchids_detail, name='detail'),
    path('orchids/<int:orchid_id>/add_watering/', views.add_watering, name='add_watering'),
    path('orchids/<int:orchid_id>/assoc_supply/<int:supply_id>/', views.assoc_supply, name='assoc_supply'),
    path('orchids/<int:orchid_id>/disassoc_supply/<int:supply_id>/', views.disassoc_supply, name='disassoc_supply'),
    path('orchids/create/', views.OrchidCreate.as_view(), name='orchids_create'),
    path('orchids/<int:pk>/update/', views.OrchidUpdate.as_view(), name='orchids_update'),
    path('orchids/<int:pk>/delete/', views.OrchidDelete.as_view(), name='orchids_delete'),
    path('supplies/create/',views.SupplyCreate.as_view(), name='supplies_create'),
    path('supplies/<int:pk>/update/',views.SupplyUpdate.as_view(), name='supplies_update'),
    path('supplies/<int:pk>/delete/',views.SupplyDelete.as_view(), name='supplies_delete'),
    path('supplies/<int:pk>/',views.SupplyDetail.as_view(), name='supply_detail'),
    path('supplies/', views.SupplyList.as_view(), name='supplies_index'),
]