from django.db.models import fields
import django_filters
from .models import *

class bookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields='__all__'