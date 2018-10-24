

# cloudcalc

cloudcalc is a team website to expose interesting homegrown Support and Success
tools to our team. It is built with [Python][0] using the
[Django Web Framework][1].

This project has the following basic apps:

* django (A High-level Python Web framework that encourages rapid development
  and clean, pragmatic design)
* DB (short desc)
* More stuff?? (short desc)

## Installation

### Quick start (using pip)

To set up a development environment quickly, first install Python 3 and pip. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv cloudcalc`
    2. `$ . cloudcalc/bin/activate`

Install all dependencies:

    3. `$ pip install -r requirements.txt`

Create local.env files

    4. `$ cd src`
    5. `$ cp my_proj/settings/local.sample.env my_proj/settings/local.env`

Run migrations:

    6. `$ python manage.py migrate`

Run dev server

    7. `$ python manage.py runserver`

### Detailed instructions (Recommended)

To set up a development environment quickly, first install Python 3. Also
install pip and pipenv. Optimized way to manage your virtualenv and package
management:

    1. `pip install pipenv`
    2. `$ pipenv intall --dev`

Switch to virtualenv:

    3. `$ pipenv shell --three`

Install all dependencies:

    4. `$ pip install -r requirements.txt`

Create local.env files

    5. `$ cd src`
    6. `$ cp my_proj/settings/local.sample.env my_proj/settings/local.env`

Run migrations:

    7. `$ python manage.py migrate`

Run dev server

    7. `$ python manage.py runserver`

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
