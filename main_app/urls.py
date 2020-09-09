from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orchids/', views.orchids_index, name='index'),
    path('orchids/<int:orchid_id>/', views.orchids_detail, name='detail'),
]