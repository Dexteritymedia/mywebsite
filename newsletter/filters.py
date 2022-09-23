from django_filters import FilterSet
from django_filters.filters import AllValuesFilter

from .models import ExtendedContact


class ContactFilter(FilterSet):
    location = AllValuesFilter()

    class Meta:
        model = ExtendedContact
        fields = ('location',)
