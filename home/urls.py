from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.Index_Handler),
    path('home/',views.Home_Hnadler,name='home'),
    path('home/create-team/',views.Create_Team_Handler,name='create-team'),
    path('home/create-group/',views.Create_Group_Handler,name='create-group'),
    path('home/more/<int:id>',views.More_Handler,name="more")
]+staticfiles_urlpatterns()
