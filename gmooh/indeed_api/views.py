from django.shortcuts import render

import os

from .models import JobAPI, JobPost


# Search
def search(request):
    # if not post - return empty form

    # if post - process form and build url

        # run the query url


        # save results to database and redirect to job listings page

    return render(request, template_name='indeed_api/search.html')


# Results page
def results(request):
    # if not post, show all listings!

    # if post - apply filter and return listings!

    return render(request, template_name='indeed_api/results.html')

# Job posting


# Create your views here.
def index(request):
    # Call api and return url
    job = JobAPI()

    job.api_key = os.environ['INDEED_PUBLISHER_API']

    job.search_must_contain = ""
    job.search_at_least_one = "django python"
    job.search_cant_contain = "senior sr"
    job.full_query = job.return_query_string()

    job.city = "Austin"
    job.state = "TX"
    job.location = job.return_location()

    final_url = job.build_url_job_search()

    api_url = final_url

    context = {
        "api_url": api_url
    }

    return render(request, 'indeed_api/index.html', context=context)
