from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/<slug>', views.details, name = 'details'),
    path('confirmed/<slug>', views.confirmed, name = 'confirmed'),

]
