from django.forms import ModelForm

from .models import JobAPI


class SearchForm(ModelForm):
    class Meta:
        model = JobAPI
        fields = ['search_must_contain', 'search_at_least_one', 'search_cant_contain', 'city', 'state']
