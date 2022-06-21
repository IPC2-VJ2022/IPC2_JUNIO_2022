from django.urls import path
from . import views

urlpatterns=[
    path('',views.elemento1,name='elemento1'),
    path('elemento2/',views.elemento2,name='elemento2')
]