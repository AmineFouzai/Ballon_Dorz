from django.shortcuts import render,redirect

# Create your views here.



def Index_Handler(request):

    return render(request,'home/index.djt')


def Home_Hnadler(request):
    return render(request,'home/home.djt')