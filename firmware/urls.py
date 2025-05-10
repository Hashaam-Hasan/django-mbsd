from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.firmware_upload, name='firmware_upload'),
    path('check/', views.check_firmware, name='firmware_check'),
    
]
