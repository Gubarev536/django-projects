from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import DateRangeWidget
from .models import Post
from django import forms


class PostFilter(FilterSet):
    dateCreation = DateFromToRangeFilter(
        lookup_expr=('icontains'),
        widget=DateRangeWidget(
            attrs={'type':'date'}
        )
    )

    class Meta:
        model = Post
        fields = {
            'author':['exact'],
            'title':['icontains'],
            'dateCreation':['exact'],
            'categoryType':['exact'],
        }