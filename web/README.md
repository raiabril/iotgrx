# iotGRX web application

This is the server for the application, it is developed using Django and REST FRAMEWORK.

## Docker

To manage the docker containers the commands are the following:

    docker-compose -f docker-compose.yml --env-file ./env/.integration.env up -d --build

## Django

### Create migrations

Update the changes in the DB to make the migrations

    python3 manage.py makemigrations

### Migrations

Apply the current migrations to the current project.

    python3 manage.py migrate

### To apply changes in the DB

We have to do again

    python3 manage.py migrate

### Create superuser

Create a superuser to access the Django administration to administer the page.

    python3 manage.py createsuperuser

## Testing

To use the Django testing.

    python3 manage.py test

To use coverage

    coverage run --source='.' manage.py test api
    coverage report
    coverage html


## Automatic client generation

Install the `npm` tool, source [here](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/apis/#an-automatically-created-openapi3-schema)

    npm install @openapitools/openapi-generator-cli -g

Launch the tool

    openapi-generator-cli generate -i schema.yml -g typescript-fetch -o ./my-api-client/

Or from the server

    openapi-generator-cli generate -i http://localhost:8000/api/schema/ -g typescript-fetch -o ./my-api-client/