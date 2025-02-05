from django_filters import rest_framework as filter
from .models import *

class customFilter(filter.FilterSet):
    class Meta:
        model = Product
        fields = {
            "category":['exact'],
            "price": ['gt','lt']
        }