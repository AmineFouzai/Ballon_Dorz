from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.Index_Handler),
    path('home/',views.Home_Hnadler,name='home')
]+staticfiles_urlpatterns()
