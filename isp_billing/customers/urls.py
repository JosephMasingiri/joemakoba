from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('<uuid:pk>/', views.customer_detail, name='customer_detail'),
    path('new/', views.customer_create, name='customer_create'),
    path('<uuid:pk>/edit/', views.customer_update, name='customer_update'),
    path('<uuid:pk>/deactivate/', views.customer_deactivate, name='customer_deactivate'),
]
