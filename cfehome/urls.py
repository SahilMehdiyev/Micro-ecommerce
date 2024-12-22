
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
