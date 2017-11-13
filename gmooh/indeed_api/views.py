from django.shortcuts import render

import os

from .models import JobAPI, JobPost


# Create your views here.
def index(request):
    # Call api and return url
    job = JobAPI()

    job.api_key = os.environ['INDEED_PUBLISHER_API']

    job.search_must_contain = "django"
    job.search_at_least_one = ""
    job.search_cant_contain = ""
    job.full_query = job.convert_search_terms_for_url()

    job.city = ""
    job.state = "ca"
    job.location = job.return_location()

    final_url = job.build_url_job_search()

    api_url = final_url

    context = {
        "api_url": api_url
    }

    return render(request, 'indeed_api/index.html', context=context)
