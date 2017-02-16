# Django 1.10 python 3 template

## Requirements

* python 3.6

## Development
Installation
```
$ python3 -m venv /path/to/venv
$ source /path/to/venv/bin/activate
$ pip install -r requirements/dev.txt
```

DB create/migrate
```
$ python manage.py migrate
```

Create admin user
```
$ python manage.py createsuperuser
```

Run server
```
$ python manage.py runserver
```

## Testing
Heroku: https://django_template.herokuapp.com
Git: https://git.heroku.com/django_template.git

### Setup

```
$ git remote add heroku https://git.heroku.com/django_template.git
$ heroku config:set DJANGO_SETTINGS_MODULE=django_template.settings.production
$ heroku config:set AWS_ACCESS_KEY_ID=<your_access_key_id>
$ heroku config:set AWS_SECRET_ACCESS_KEY=<your_access_key_secret>
$ heroku config:set AWS_STORAGE_BUCKET_NAME=<your_bucket_name>
$ heroku config:set SECRET_KEY=<secret_key>
$ heroku addons:create papertrail:choklad
$ heroku addons:create heroku-postgresql:hobby-dev
$ git push heroku master
```

## Run commands, e.g. migrate

```
$ heroku run python manage.py CMD --settings django_template.settings.production
$ heroku run python manage.py migrate
```

