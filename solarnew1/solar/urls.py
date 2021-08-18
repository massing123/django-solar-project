
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    path('home',include('app1.urls')),
    path('contactus',include('app1.urls')),
    path('material_inspection',include('app1.urls')),
    path('plant_testing',include('app1.urls')),
    path('manpower_equi',include('app1.urls')),
    path('Project_Registration',include('app1.urls')),
    path('signupme',include('app1.urls')),
    

    
]
