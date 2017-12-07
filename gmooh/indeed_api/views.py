import os

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404

from .forms import SearchForm
from .models import JobAPI, JobPost
from .utils.api_runner import api_main


def index(request):

    searches = JobAPI.objects.all()

    context = {
        "searches": searches,
    }

    return render(request, 'indeed_api/index.html', context=context)


def search(request):
    search_form = SearchForm()

    # if post - process form and build url with form data
    # otherwise, return an empty search form
    if request.method == 'POST':
        submitted_form = SearchForm(request.POST)
        if submitted_form.is_valid():
            form_data = submitted_form.save(commit=False)

            form_data.search_must_contain = submitted_form.cleaned_data['search_must_contain']
            form_data.search_at_least_one = submitted_form.cleaned_data['search_at_least_one']
            form_data.search_cant_contain = submitted_form.cleaned_data['search_cant_contain']
            form_data.full_query = form_data.return_query_string()

            form_data.city = submitted_form.cleaned_data['city']
            form_data.state = submitted_form.cleaned_data['state']
            form_data.location = form_data.return_location()

            form_data.url_for_api = form_data.build_url_job_search()

            if JobAPI.objects.filter(url_for_api=form_data.url_for_api).exists():
                # Search already exists, update timestamp
                form_data.url_updated()
            else:
                form_data.save()
                return redirect(reverse("indeed_api:index"))

    context = {
        'search_form': search_form
    }

    return render(request, template_name='indeed_api/search.html', context=context)


def results(request):
    # get newest listings, fresh off the press
    api_main()

    # get all job listings
    jobs = JobPost.objects.filter(listing_hidden=False)

    # if post - filter by categories

    context = {
        'jobs': jobs,
    }

    return render(request, template_name='indeed_api/results.html', context=context)


def hide_listing(request, listing_pk):
    listing = get_object_or_404(JobPost, pk=listing_pk)
    listing.listing_hidden = True
    listing.save()

    return HttpResponseRedirect(reverse('indeed:results'))
