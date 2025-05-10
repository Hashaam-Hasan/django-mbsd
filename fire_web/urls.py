"""
URL configuration for fire_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""





from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),  # monitoring app
    path('firmware/', include(('firmware.urls', 'firmware'), namespace='firmware')),  # firmware app



    # path('admin/', admin.site.urls),
    # path('', include('monitoring.urls')),
    # path('firmware/', include('firmware.urls')),

    # path('admin/', admin.site.urls),
    # path('firmware/', include('firmware.urls')),


    path('', include('monitoring.urls')),    # Sensor data pages (home, details, about)
    # path('firmware/', include(('firmware.urls', 'firmware'), namespace='firmware')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)