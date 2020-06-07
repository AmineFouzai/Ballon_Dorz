from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/',include('accounts.urls'),name="accounts"),
    path('',include('home.urls'),name='home')
]



