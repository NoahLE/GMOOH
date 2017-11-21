# Get Me Out Here! (GMOOH)

GMOOH an application which calls the Indeed job API and displays the listings locally on the user's computer. My hope is this application will allow significantly better filtering, tracking, and will eventually plug into other job listing networks.

## Getting started

To begin working on this project you'll need to install `Python 3.X`. After that, create a Python `virtual environment` and clone the project's files into a directory.

Then, install the required files by running `pip install -r requirements/local.txt`. If you haven't done so, you can create a database using the `createdb` command. To wire up the login settings either customize the `env.example` with your database settings or update the `base.py` file in `config/settings/base.py` with something like the following: 

```python
DATABASES = {
    # Use this if you are using the .env or env.example file
    # 'default': env.db('DATABASE_URL', default='postgres:///<db-name>'),

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db-name>',
        'USER': '<db-user>',
        'PASSWORD': '<user-password>',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

## The technology stack

- Python 3.X
- PostgreSQL 10
- Django 1.11
- and the Python libraries: Requests

## Caveats

This project is a work in progress. Please contact me if you find any bugs, have suggestions, or have questions.