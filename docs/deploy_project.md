# Deploiement du projet

Toutes les opérations suivantes se font depuis le user unix de developpement

## Récupération du projet github

```
mkdir dev
cd dev
git clone https://github.com/sebcb1/OraTune.git
cd OraTune
git config --global user.email "sebastienbrillard@icloud.com"
git config --global user.name  "Sébastien Brillard"
git config --global push.default simple
```

Toutes les commandes suivantes sont faites depuis le répertoire:
`dev/OraTune`

## Deploiement des packages python from scratch

Depuis le user de developement, création de l'env pipenv:
`pipenv --python /usr/bin/python3`

Ajout des packages python:
```
pipenv install django psycopg2-binary celery django-celery-results scikit-optimize cx-oracle
pipenv install Sphinx
pipenv install nose pylint --dev
```

## Deploiement des packages python depuis le clone du repo GitHub

```
cd dev/OraTune
pipenv install
```

## Démarrer le projet






## Initialisation du projet Django

Pour information ce chapitre contient toutes les commandes qui on servit à l'initialisation du projet.
Toutes ces commandes sont depuis dev/OraTune.

Initialisation du projet web:
```
mkdir dev/OraTune
cd dev/OraTune
pipenv run django-admin.py startproject app
```

Editer ./app/settings.py:
```
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django_celery_results',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oratune',
        'USER': 'oratune',
        'PASSWORD': 'oratune',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'
```

Mise ne place de la doc Sphinx:
```
mkdir dev/OraTune/sphinx
mkdir dev/OraTune/app/app/static/docs
cd dev/OraTune/sphinx
pipenv run sphinx-quickstart
pipenv run sphinx-build -b html . ../app/app/static/docs/
```

Population de la bdd:
```
cd dev/OraTune/app
pipenv run ./manage.py migrate
pipenv run ./manage.py createsuperuser
pipenv run ./manage.py migrate django_celery_results
```

### Quelques commandes django


