from django.shortcuts import render

# Create your views here.
def elemento1(request):
    return render(request,'blog/elemento1.html',{})

def elemento2(request):
    return render(request,'blog/elemento2.html',{})

    