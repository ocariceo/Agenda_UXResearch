from django.contrib import admin
from django.urls import path, include
from teamux import views

urlpatterns = [
    path('', include('teamux.urls')),
    path('admin/', admin.site.urls),
]
