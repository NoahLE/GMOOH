import os

from django.shortcuts import render

from .forms import SearchForm
from .models import JobAPI


def index(request):
    # Not sure which logic will go here yet

    context = {
        "api_url": ":D"
    }

    return render(request, 'indeed_api/index.html', context=context)


# Search
def search(request):
    # if not post - return empty form
    search_form = SearchForm()
    final_url = ''

    # if post - process form and build url
    if request.method == 'POST':
        submitted_form = SearchForm(request.POST)
        if submitted_form.is_valid():
            api_search = JobAPI()
            api_search.api_key = os.environ['INDEED_PUBLISHER_API']

            api_search.search_must_contain = submitted_form.cleaned_data['search_must_contain']
            api_search.search_at_least_one = submitted_form.cleaned_data['search_at_least_one']
            api_search.search_cant_contain = submitted_form.cleaned_data['search_cant_contain']
            api_search.full_query = api_search.return_query_string()

            api_search.city = submitted_form.cleaned_data['city']
            api_search.state = submitted_form.cleaned_data['state']
            api_search.location = api_search.return_location()

            final_url = api_search.build_url_job_search()


    # run the query url


    # Call api and return url


    # URl building mechanics



    # save results to database and redirect to job listings page
    context = {
        'search_form': search_form,
        'final_url': final_url
    }

    return render(request, template_name='indeed_api/search.html', context=context)  # Results page


def results(request):
    # if not post, show all listings!

    # if post - apply filter and return listings!

    return render(request, template_name='indeed_api/results.html')

# Job posting
