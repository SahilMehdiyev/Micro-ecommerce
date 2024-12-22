
from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.product_create_view, name='create_product'),
]
