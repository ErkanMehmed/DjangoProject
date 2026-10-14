from django.urls import path

from manufacturers.views import ManufacturersListView, ManufacturerDetailView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView

urlpatterns = [
    path("", ManufacturersListView.as_view(), name="manufacturers-list"),
    path('detail/<int:pk>/', ManufacturerDetailView.as_view(), name="manufacturers-detail"),
    path('create/', ManufacturerCreateView.as_view(), name="manufacturers-create"),
    path('update/<int:pk>/', ManufacturerUpdateView.as_view(), name="manufacturers-update"),
    path('delete/<int:pk>/', ManufacturerDeleteView.as_view(), name="manufacturers-delete"),
]