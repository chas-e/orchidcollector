from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orchids/', views.orchids_index, name='index'),
    path('orchids/<int:orchid_id>/', views.orchids_detail, name='detail'),
    path('orchids/create/', views.OrchidCreate.as_view(), name='orchids_create'),
    path('orchids/<int:pk>/update/', views.OrchidUpdate.as_view(), name="orchids_update"),
    path('orchids/<int:pk>/delete/', views.OrchidDelete.as_view(), name="orchids_delete"),
]