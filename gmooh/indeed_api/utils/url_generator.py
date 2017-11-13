class IndeedAPI:
    def __init__(self, api_key):
        # API Key
        self.publisher = api_key

        # Base API urls
        self.url_search = "http://api.indeed.com/ads/apisearch?"
        self.url_jobs = "http://api.indeed.com/ads/apigetjobs?"

        # Query
        self.search_all = ""
        self.search_at_least_one = ""
        self.search_none = ""
        self.query = self.return_query_string()

        # Location
        self.city = ""
        self.state = ""
        self.location = self.return_location()

        # Sort by relevance or date
        self.sort = "date"

        # API format output
        # json or xml
        self.format = "json"

        # Radius from search location
        self.radius = "15"

        # Site type
        # "jobsite", "employer", blank for both
        self.site_type = ""

        # Job type
        # "fulltime", "parttime", "contract", "internship", "temporary"
        self.job_type = ""

        # Start results at this number
        self.results_start = ""

        # Max number of results
        # 10, 20, 30, 40, 50
        self.results_limit = "50"

        # Number of days back to search
        # any, 1, 3, 7, 15
        self.post_age = "7"

        # Filter duplicates
        # Off - 0, on - 1
        self.toggle_filter = "1"

        # Show lat long coodinates
        # Off - 0, on - 1
        self.return_latlong = "0"

        # Search within a country
        self.country = "us"

        # Group requests to a specific channel
        # This can be set on your Indeed developer page
        self.channel = ""

        # IP of the end-user to whom the job results are displayed to
        self.userip = "1.2.3.4"

        # Browser type of the end user
        self.useragent = "Mozilla/%2F4.0%28Firefox%29"

        # API Version
        self.version = "2"

    def return_location(self):
        # Returns a url-friendly version of the location
        # examples: Austin%2C+TX / San+Francisco%2C+CA

        return self.city + "%2C+" + self.state

    def convert_for_url(self, url_terms="", url_type=""):
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
        if self.search_all:
            search_url += self.convert_for_url(url_terms=self.search_all,
                                               url_type="all")
        if self.search_at_least_one:
            if self.search_all:
                search_url += "+"
            search_url += self.convert_for_url(url_terms=self.search_at_least_one,
                                               url_type="one")
        if self.search_none:
            if self.search_all or self.search_at_least_one:
                search_url += "+"
            search_url += self.convert_for_url(url_terms=self.search_none,
                                               url_type="none")

        return search_url

    def build_url_job_search(self):
        # Returns a search url for all job listings in a certain area
        built_url = self.url_search + \
                    "publisher=" + self.publisher + "&" + \
                    "q=" + self.query + "&" + \
                    "l=" + self.location + "&" + \
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
        built_url = self.url_jobs + "&" + \
                    "publisher=" + self.publisher + "&" + \
                    "jobkeys=" + job_keys + "&" + \
                    "v=" + self.version
        return built_url
