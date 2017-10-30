import os

from api_scrapers.api_scraper_indeed import IndeedAPI

API_key = os.environ['INDEED_PUBLISHER_API']

if __name__ == "__main__":
    print("hello")
    d = IndeedAPI(api_key=API_key)
    d.location = "San+Francisco+Bay+Area%2C"
    d.query = "java+manager"
    print(d.api_search_job())
