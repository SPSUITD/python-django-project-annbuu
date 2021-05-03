from django.urls import path
from . import views


urlpatterns = [
  path('', views.firstroom, name='firstroom'),
  path('second', views.secondroom, name='secondroom'),
  path('third', views.thirdroom, name='thirdroom'),
  path('fourth', views.fourthroom, name='fourthroom'),
  path('fifth', views.fifthroom, name='fifthroom'),
]