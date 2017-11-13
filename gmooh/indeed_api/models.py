from django.db import models


class JobAPI(models.Model):
    # API Key
    api_key = models.CharField(default="")

    # Query
    search_must_contain = models.CharField(default="")
    search_at_least_one = models.CharField(default="")
    search_cant_contain = models.CharField(default="")
    full_query = models.CharField(default="")

    # Location
    city = models.CharField(default="")
    state = models.CharField(default="")
    location = models.CharField(default="")

    # Sort by relevance or date
    sort = models.CharField(default="date")

    # API format output
    # json or xml
    format = models.CharField(default="json")

    # Radius from search location in miles
    radius = "15"

    # Site type
    # "jobsite", "employer", blank for both
    site_type = models.CharField(default="")

    # Job type
    # "fulltime", "parttime", "contract", "internship", "temporary"
    job_type = models.CharField(default="")

    # Start results at this number
    results_start = models.CharField(default="")

    # Max number of results
    # 10, 20, 30, 40, 50
    results_limit = models.CharField(default="50")

    # Number of days back to search
    # any, 1, 3, 7, 15
    post_age = models.CharField(default="7")

    # Filter duplicates
    # Off - 0, on - 1
    toggle_filter = models.CharField(default="1")

    # Show lat long coodinates
    # Off - 0, on - 1
    return_latlong = models.CharField(default="0")

    # Search within a country
    country = models.CharField(default="us")

    # Group requests to a specific channel
    # This can be set on your Indeed developer page
    channel = models.CharField(default="")

    # IP of the end-user to whom the job results are displayed to
    userip = models.CharField(default="1.2.3.4")

    # Browser type of the end user
    useragent = models.CharField(default="Mozilla/%2F4.0%28Firefox%29")

    # API Version
    version = models.CharField(default="2")

    def return_location(self):
        # Returns a url-friendly version of the location
        # examples: Austin%2C+TX / San+Francisco%2C+CA

        return self.city + "%2C+" + self.state

    def convert_search_terms_for_url(self, url_terms="", url_type=""):
        # Returns the user's search terms formatted for API call
        # all of these words - java+manager
        # at least one of these - %28python+or+javascript%29
        # none of these words - -sr+-senior

        if url_type == "all" or url_type == "one":
            url_terms = url_terms.replace(" ", "+").lower()
            if url_type == "one":
                url_terms = "%28" + url_terms + "%29"
        elif url_type == "none":
            url_terms = "-" + url_terms.replace(" ", "+-").lower()
        else:
            pass
        return url_terms

    def return_query_string(self):
        # Converts search terms for API use
        # %28javascript+or+python%29+-senior+-sr

        search_url = ""
        if self.search_must_contain:
            search_url += self.convert_search_terms_for_url(url_terms=self.search_must_contain,
                                               url_type="all")
        if self.search_at_least_one:
            if self.search_must_contain:
                search_url += "+"
            search_url += self.convert_search_terms_for_url(url_terms=self.search_at_least_one,
                                               url_type="one")
        if self.search_cant_contain:
            if self.search_must_contain or self.search_at_least_one:
                search_url += "+"
            search_url += self.convert_search_terms_for_url(url_terms=self.search_cant_contain,
                                               url_type="none")

        return search_url

    def build_url_job_search(self):
        # Returns a search url for all job listings in a certain area
        built_url = "http://api.indeed.com/ads/apisearch?" + \
                    "publisher=" + self.api_key + "&" + \
                    "q=" + self.return_query_string() + "&" + \
                    "l=" + self.return_location() + "&" + \
                    "sort=" + self.sort + "&" + \
                    "radius=" + self.radius + "&" + \
                    "st=" + self.site_type + "&" + \
                    "jt=" + self.job_type + "&" + \
                    "start=" + self.results_start + "&" + \
                    "limit=" + self.results_limit + "&" + \
                    "post_age=" + self.post_age + "&" + \
                    "filter=" + self.toggle_filter + "&" + \
                    "return_latlong=" + self.return_latlong + "&" + \
                    "co=" + self.country + "&" + \
                    "chnl=" + self.channel + "&" + \
                    "userip=" + self.userip + "&" + \
                    "useragent=" + self.useragent + "&" + \
                    "v=" + self.version
        return built_url

    def build_url_job_list(self, job_keys=""):
        built_url = "http://api.indeed.com/ads/apigetjobs?" + "&" + \
                    "publisher=" + self.api_key + "&" + \
                    "jobkeys=" + job_keys + "&" + \
                    "v=" + self.version
        return built_url


class JobPost(models.Model):
    job_title = models.CharField(default='')
    company = models.CharField(default='')
    city = models.CharField(default='')
    state = models.CharField(default='')
    country = models.CharField(default='')
    language = models.CharField(default='')
    formatted_location = models.CharField(default='')
    source = models.CharField(default='')
    date = models.CharField(default='')
    snippet = models.CharField(default='')
    url = models.CharField(default='')
    onmousedown = models.CharField(default='')
    job_key = models.CharField(default='')
    sponsored = models.CharField(default='')
    expired = models.CharField(default='')
    indeed_apply = models.CharField(default='')
    formatted_location_full = models.CharField(default='')
    formatted_relative_time = models.CharField(default='')

    def __str__(self):
        return self.job_title
