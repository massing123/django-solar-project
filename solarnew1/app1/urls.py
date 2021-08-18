
from typing import ValuesView
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('contactus',views.contactus,name="contactus"),
    path('material_inspection',views.material_inspection,name="material_inspection"),
    path('plant_testing',views.plant_testing,name="plant_testing"),
    path('manpower_equi',views.manpower_equi,name="manpower_equi"),
    path('Project_Registration',views.Project_Registration,name="Project_Registration"),
    path('signupme',views.signupme,name="signupme"),
    path('logout',views.logout,name="logout"),
    
    
    ]
