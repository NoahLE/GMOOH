import os

from indeed_api.utils import IndeedAPI

API_key = os.environ['INDEED_PUBLISHER_API']

if __name__ == "__main__":
    print("=====| Indeed API URL generator |=====")
    d = IndeedAPI(api_key=API_key)

    # Search terms
    # search_all - must contain all these terms
    # at_least_one - must contain at least one of these terms
    # none - cannot contain these terms
    d.search_all = ""
    d.search_at_least_one = "python javascript"
    d.search_none = "senior sr"

    # Location
    d.city = "Austin"
    d.state = "TX"

    # Job type and advance attributes
    d.job_type = "fulltime"
    d.post_age = "7"
    d.results_limit = "50"
    d.results_start = ""
    d.return_latlong = "1"

    # Build location and search results
    d.query = d.return_query_string()
    d.location = d.return_location()

    # Return result
    print(d.build_url_job_search())
