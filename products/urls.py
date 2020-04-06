from django.urls import path
from .views import products_list, product_create, product_update
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    path("",  products_list),
    path("create/", product_create),
    path("update/<int:pk>", product_update)
]

urlpatterns = format_suffix_patterns(urlpatterns)