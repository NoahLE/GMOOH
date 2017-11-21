import json

import requests

from indeed_api.models import JobAPI, JobPost


def build_batch_urls(url_object, total_results):
    number_of_batches = round(total_results / 25)

    for batch in range(number_of_batches):
        new_batch = url_object
        new_batch.pk = None
        new_batch.results_start = batch * 25
        new_batch.build_url_job_search()
        new_batch.save()


def run_api_urls():
    urls_to_run = JobAPI.objects.filter(url_run=False)

    for url in urls_to_run:
        result = requests.get(url.url_for_api)
        if result.status_code == 200:
            url.url_run = True

            data_to_parse = result.text
            parsed_data = json.loads(data_to_parse)

            start = parsed_data['start']
            end = parsed_data['end']
            total_results = parsed_data['totalResults']

            if total_results > 25:
                build_batch_urls(url_object=url,
                                 total_results=total_results)

            results = parsed_data['results']

            for result in results:
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
