import os

from api_scrapers.api_scraper_indeed import IndeedAPI

API_key = os.environ['INDEED_PUBLISHER_API']

if __name__ == "__main__":
    print("hello")
    d = IndeedAPI(api_key=API_key)
    d.location = "Austin%2C+TX"
    d.search_all = ""
    d.search_at_least_one = "python javascript"
    d.search_none = "senior sr"
    d.query = d.return_query_string()
    print(d.build_url_job_search())
