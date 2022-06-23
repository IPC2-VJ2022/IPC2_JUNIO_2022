from django.urls import path
from . import views
urlpatterns = [
    path('', views.elemento1, name='elemento1'),
]