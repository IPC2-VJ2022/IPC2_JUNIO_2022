from django.shortcuts import render
from .models import Empleado
import requests
# pip install requests

# Create your views here.
def elemento1(request):
    resp =requests.get('http://localhost:9000/empleados')
    datos=resp.json()
    return render(request,'blog/elemento1.html',{'variable':datos})


