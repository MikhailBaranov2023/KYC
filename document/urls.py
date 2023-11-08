from document.apps import DocumentConfig
from django.urls import path

from document.views import DocumentUpdateDestroyAPIView, DocumentCreateAPIView, DocumentVerifiedAPIView

app_name = DocumentConfig.name

urlpatterns = [
    path('<int:pk>/', DocumentUpdateDestroyAPIView.as_view(), name='document_api_view'),
    path('add/', DocumentCreateAPIView.as_view(), name='document_create'),
    path('verificated/<int:pk>/', DocumentVerifiedAPIView.as_view(), name='document_verified'),
]
