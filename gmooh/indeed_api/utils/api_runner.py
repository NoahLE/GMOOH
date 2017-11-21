import json

import requests

from indeed_api.models import JobAPI, JobPost


def run_sample_api():
    with open('indeed_api/utils/sample.json', 'r') as f:
        data = json.load(f)

        start = data['start']
        end = data['end']
        pageNumber = data['pageNumber']
        results = data['results']

        for result in results:
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
            pageNumber = parsed_data['pageNumber']
            results = parsed_data['results']

            for result in results:
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
