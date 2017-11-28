import json
from math import ceil

import requests

from indeed_api.models import JobAPI, JobPost


# Takes the results from the Indeed API and saves each listing to the database
# Helper function for - run_api()
def save_posts_to_database(data):
    for result in data:
        if not JobPost.objects.filter(job_key=result['jobkey']).exists():
            JobPost.objects.get_or_create(
                job_title=result['jobtitle'],
                company=result['company'],
                source=result['source'],
                language=result['language'],

                city=result['city'],
                state=result['state'],
                country=result['country'],
                formatted_location=result['formattedLocationFull'],

                date=result['date'],
                snippet=result['snippet'],
                job_key=result['jobkey'],
                url=result['url'],

                sponsored=result['sponsored'],
                expired=result['expired'],
                onmousedown=result['onmousedown']
            )


# Builds URLs based on the number of results from the API call
# Helper function for - run_api()
def build_batch_urls(url_object, total_results):
    number_of_batches = int(ceil(total_results / 25))

    for batch in range(1, number_of_batches):
        new_batch = url_object
        new_batch.pk = None
        new_batch.url_type = "batch"
        new_batch.results_start = str(batch * 25)
        new_batch.build_url_job_search()

        # If the batch URL doesn't exist, save it
        if not JobAPI.objects.filter(url_type=new_batch.url_type,
                                     results_start=new_batch.results_start,
                                     url_for_api=new_batch.url_for_api).exists():
            new_batch.save()


# Runs each query url through the API and returns the number of results and each result
def run_api(urls):
    for url in urls:
        result = requests.get(url.url_for_api)
        if result.status_code == 200:
            data_to_parse = result.text
            parsed_data = json.loads(data_to_parse)

            url.raw_data = parsed_data
            url.url_run = True
            url.save()

            total_results = parsed_data['totalResults']
            results = parsed_data['results']

            build_batch_urls(url_object=url, total_results=total_results)
            save_posts_to_database(data=results)


def api_main():
    seed_urls_to_run = JobAPI.objects.filter(url_type="seed", )
                                            # url_run=False,)


    batch_urls_to_run = JobAPI.objects.filter(url_type="batch", )
                                            # url_run=False,)

    run_api(seed_urls_to_run)
    run_api(batch_urls_to_run)
