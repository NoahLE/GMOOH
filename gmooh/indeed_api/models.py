from django.db import models


class JobAPI(models.Model):
    # API Key
    api_key = models.CharField(default="", max_length=50)

    # Query
    search_must_contain = models.CharField( max_length=350, default="")
    search_at_least_one = models.CharField(max_length=350, default="")
    search_cant_contain = models.CharField(max_length=350, default="")
    full_query = models.CharField(max_length=350, default="")

    # Location
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=2, default="")
    location = models.CharField(max_length=350, default="")

    # Sort by relevance or date
    sort = models.CharField(max_length=15, default="date")

    # API format output
    # json or xml
    format = models.CharField(max_length=4, default="json")

    # Radius from search location in miles
    radius = models.CharField(max_length=4, default="15")

    # Site type
    # "jobsite", "employer", blank for both
    site_type = models.CharField(max_length=25, default="")

    # Job type
    # "fulltime", "parttime", "contract", "internship", "temporary"
    job_type = models.CharField(max_length=350, default="fulltime")

    # Start results at this number
    results_start = models.CharField(max_length=4, default="")

    # Max number of results
    # 10, 20, 30, 40, 50
    results_limit = models.CharField(max_length=4, default="50")

    # Number of days back to search
    # any, 1, 3, 7, 15
    post_age = models.CharField(max_length=4, default="7")

    # Filter duplicates
    # Off - 0, on - 1
    toggle_filter = models.CharField(max_length=1, default="1")

    # Show lat long coodinates
    # Off - 0, on - 1
    return_latlong = models.CharField(max_length=1, default="0")

    # Search within a country
    country = models.CharField(max_length=25, default="us")

    # Group requests to a specific channel
    # This can be set on your Indeed developer page
    channel = models.CharField(max_length=350, default="")

    # IP of the end-user to whom the job results are displayed to
    userip = models.CharField(max_length=25, default="1.2.3.4")

    # Browser type of the end user
    useragent = models.CharField(max_length=350, default="Mozilla/%2F4.0%28Firefox%29")

    # API Version
    version = models.CharField(max_length=4, default="2")

    def return_location(self):
        # Returns a url-friendly version of the location
        # examples: Austin%2C+TX / San+Francisco%2C+CA

        return self.city + "%2C+" + self.state

    def convert_search_terms_for_url(self, url_terms="", url_type=""):
        # Helper function for return_query_string()
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
                    "q=" + self.full_query + "&" + \
                    "l=" + self.location + "&" + \
                    "sort=" + self.sort + "&" + \
                    "radius=" + self.radius + "&" + \
                    "st=" + self.site_type + "&" + \
                    "jt=" + self.job_type + "&" + \
                    "start=" + self.results_start + "&" + \
                    "limit=" + self.results_limit + "&" + \
                    "fromage=" + self.post_age + "&" + \
                    "filter=" + self.toggle_filter + "&" + \
                    "latlong=" + self.return_latlong + "&" + \
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

    def __str__(self):
        return self.city


class JobPost(models.Model):
    job_title = models.CharField(max_length=350, default='')
    company = models.CharField(max_length=350, default='')
    city = models.CharField(max_length=350, default='')
    state = models.CharField(max_length=350, default='')
    country = models.CharField(max_length=350, default='')
    language = models.CharField(max_length=350, default='')
    formatted_location = models.CharField(max_length=350, default='')
    source = models.CharField(max_length=350, default='')
    date = models.CharField(max_length=350, default='')
    snippet = models.CharField(max_length=350, default='')
    url = models.CharField(max_length=350, default='')
    onmousedown = models.CharField(max_length=350, default='')
    job_key = models.CharField(max_length=350, default='')
    sponsored = models.CharField(max_length=350, default='')
    expired = models.CharField(max_length=350, default='')
    indeed_apply = models.CharField(max_length=350, default='')
    formatted_location_full = models.CharField(max_length=350, default='')
    formatted_relative_time = models.CharField(max_length=350, default='')

    def __str__(self):
        return self.job_title
