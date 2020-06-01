from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls'),name="accounts"),
    path('',include('home.urls'),name='home')
]
