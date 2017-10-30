class IndeedAPI:
    def __init__(self, api_key):
        # API Key
        self.publisher = api_key

        # Base API urls
        self.url_search = "http://api.indeed.com/ads/apisearch?"
        self.url_jobs = "http://api.indeed.com/ads/apigetjobs?"

        # Query
        # all of these words - java+manager
        # at least one of these - %28python+or+javascript%29
        # none of these words - -sr+-senior
        self.search_all = ""
        self.search_least = ""
        self.search_none = ""
        self.query = self.return_query_string()

        # Location
        self.city = ""
        self.state = ""
        self.location = self.return_location()

        # Sort by relevance or date
        self.sort = "date"

        # Radius from search location
        self.radius = "10"

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
        self.results_limit = ""

        # Number of days back to search
        # any, 1, 3, 7, 15
        self.fromage = "1"

        # Filter duplicates // off - 0, on - 1
        self.toggle_filter = "1"

        # Show lat long coodinates // off - 0, on - 1
        self.latlong = "0"

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
        # examples: Austin%2C+TX / San+Francisco%2C+CA
        return self.city + "%2C+" + self.state

    def return_query_string(self):
        return self.search_all + self.search_least + self.search_none

    # Returns a search url for all job listings in a certain area
    def api_search_job(self):
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
                    "fromage=" + self.fromage + "&" + \
                    "filter=" + self.toggle_filter + "&" + \
                    "latlong=" + self.latlong + "&" + \
                    "co=" + self.country + "&" + \
                    "chnl=" + self.channel + "&" + \
                    "userip=" + self.userip + "&" + \
                    "useragent=" + self.useragent + "&" + \
                    "v=" + self.version
        return built_url

    def api_jobs_list(self, jobkeys=""):
        built_url = self.url_jobs + \
                    "publisher=" + self.publisher + \
                    "jobkeys=" + jobkeys + \
                    "v=" + self.version
        return built_url
