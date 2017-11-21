import requests
import json
import os

from indeed_api.models import JobAPI, JobPost


def run_api_urls():
    with open('indeed_api/utils/sample.json', 'r') as f:
        data = json.load(f)

        start = data['start']
        end = data['end']
        pageNumber = data['pageNumber']

        # seems to max out at 25 - need loop for batches
        total_results = data['totalResults']

        results = data['results']

        for result in results:
            job_listing = JobPost.objects.get_or_create(
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

# run_api_urls()

# urls_to_run = JobAPI.objects.filter(url_run=False)
# for url in urls_to_run:
# result = requests.get(url.url_for_api)
# with open('sample.json', 'r') as f:
#     result = json.load(f)
#     if result.status_code == 200:
#         data_to_parse = result.text
#         parsed_data = json.loads(data_to_parse)

#         results_returned = parsed_data['totalResults']
#         results_start = parsed_data['start']
#         results_end = parsed_data['end']
#         results_listings = parsed_data['results']

#         print(results_listings)
