# iotGRX web application

This is the server for the application, it is developed using Django and REST FRAMEWORK.

## Docker

To manage the docker containers the commands are the following:

    docker-compose -f docker-compose.yml --env-file ./.Docker/.test.env up -d --build

django-admin startapp movies

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

### Fields

- null = False -> Puede ser falso.
- blank = True -> Puede ser vacío.
- unique = True -> Tiene que ser único.
- default = "Ejemplo" -> Es un valor por defecto si no se provee.
- choices = [] -> Set of values that will be accepted.

### Field types

- CharField -> Chars
- TextField -> More chars
- BigIntegerField -> If it's big.
- DecimalField -> Has decimals. (decimal_places=2, max_digits=10)
- IntegerField -> Normal integer.
- FloatField -> The difference is in Python
- DateField -> To store dates in the Database. (auto_now = True or only when add auto_now_add = True)
- TimeField -> To store time in our DB.
- DateTimeField -> Date and time in one field.
- FileField(upload_to='covers/') -> Save the file
- ImageField -> It is the same but only images.
- EmailField -> Store emails.
- BooleanField -> To store if it's True / False.
