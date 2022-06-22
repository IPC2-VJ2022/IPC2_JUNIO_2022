from django.shortcuts import render

# Definimos un elemento1
def elemento1(request):
    return render(request,'blog/elemento1.html',{}) 

# Definimos un elemento2
def elemento2(request):
    return render(request,'blog/elemento2.html',{}) 

