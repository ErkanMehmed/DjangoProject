from django.urls import path
from vehicles import views

urlpatterns = [
    path('', views.VehicleListView.as_view(), name='vehicle-list'),
    path('create/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('detail/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('update/<int:pk>/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),
    path('feature/', views.FeatureListView.as_view(), name='feature-list'),
    path('feature/create/', views.FeatureCreateView.as_view(), name='feature-create'),
]