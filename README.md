# Django 1.10 python 3 template

## Requirements

* python 3.6

## Development
Installation
```
$ python3 -m venv /path/to/venv
$ pip install -r requirements/dev.txt
```

Run server
```
$ source /path/to/venv/bin/activate
$ python manage.py runserver
```

## Testing
Heroku: https://django_template.herokuapp.com
Git: https://git.heroku.com/django_template.git
```
$ heroku run python manage.py CMD --settings django_template.settings.production
$ heroku run python manage.py migrate
```
