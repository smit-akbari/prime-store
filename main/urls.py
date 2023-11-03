from django.urls import path
from .views import *

# Create your tests here.
urlpatterns = [
    path('', dashboard_view, name='dashboard_view'),
    path('add_product/',add_product,name='add_product'),
    path('edit_product/<int:product_id>/',edit_product,name='edit_product'),
    path('delete_product/<int:product_id>/',delete_product,name='delete_product')
]