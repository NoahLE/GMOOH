# API Scraping and Parsing

## Setup

To run the application, you're going to have to add the following variables to your environment.

If you are using a virtualenv (recommended method), add `INDEED_PUBLISHER_API` to your virtual environments `postactive` and `predeactivate` files.

If you are using Pycharm, add the environmental variables to the run/debug settings.

postactive
```bash
export INDEED_PUBLISHER_API="Your key here"
```

predeactivate
```bash
unset INDEED_PUBLISHER_API
```