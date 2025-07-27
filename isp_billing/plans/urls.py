from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_list, name='plan_list'),
    path('<int:pk>/', views.plan_detail, name='plan_detail'),
    path('new/', views.plan_create, name='plan_create'),
    path('<int:pk>/edit/', views.plan_update, name='plan_update'),
    path('<int:pk>/delete/', views.plan_delete, name='plan_delete'),
]
