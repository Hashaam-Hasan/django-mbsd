
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/sensor-data/', views.get_sensor_data, name='sensor_data'),


    path('details/', views.details, name='details'),
    path('about/', views.about, name='about'),
    # path('firmware/upload/', views.firmware_upload , name='firmware_upload'),

    # path('firmware/upload/', views.firmware_upload, name='firmware_upload'),

    # path('post-data/', views.post_data, name='post_data'),  # <-- Add this line


    path('', views.sensor_data_view, name='sensor-data'),



    path('api/sensor-data/', views.sensor_data, name='sensor-data'),
    path('api/sensor-history/', views.sensor_history, name='sensor-history'),



    path('livedata/', views.live, name='live'),
    path('live/', views.live, name='live'),
    path('api/get_latest_data/', views.get_latest_data, name='get_latest_data'),

]