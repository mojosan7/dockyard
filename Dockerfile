# Pull base image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /code

# Set work directory
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY ./src/dockyard/settings/local.sample.env /code/src/dockyard/settings/local.env

RUN python /code/src/manage.py migrate
# Run python /code/random-scripts/db_setup.py


# Install dependencies
#RUN pip install pipenv
#COPY ./Pipfile /code/Pipfile
#COPY ./requirements/development.txt /code/requirements.txt
#RUN pipenv install --system --skip-lock
#RUN pipenv install -r requirements.txt

# Copy project
#COPY . /code/
