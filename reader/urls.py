from django.urls import path
from .views import render_pdf_view, DocumentListView, document_render_pdf_view

app_name = 'reader'

urlpatterns = [
    path('', DocumentListView.as_view(), name='document-testview'),
    path('test/', render_pdf_view, name='test-view'),
    path('document/<pk>/', document_render_pdf_view, name='pdf-viewer'),
    ]