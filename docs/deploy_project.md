# Deploiement du projet

Toutes les opérations suivantes se font depuis le user unix de developpement

## Récupération du projet github

```
mkdir dev
cd dev
git clone https://github.com/sebcb1/OraTune.git
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

## Deploiement des packages python depuis 

## Initialisation du projet Django

Pour information ce chapitre contient toutes les commandes qui on servit à l'initialisation du projet.
Toutes ces commandes sont depuis dev/OraTune.

Initialisation du projet web:
```
mkdir dev/OraTune
cd dev/OraTune
pipenv run django-admin.py startproject app
```

Editer ./web/settings.py:
```
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'OraTune',
        'USER': 'OraTune',
        'PASSWORD': 'OraTune',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'
```

Population de la bdd:
```
cd cd dev/OraTune/app
pipenv run ./manage.py migrate
pipenv run ./manage.py createsuperuser
pipenv run ./manage.py migrate django_celery_results
```

Mise ne place de la doc Sphinx:
```
cd dev/OraTune/app
pipenv run sphinx-quickstart
cd OraTune/sphinx
pipenv run sphinx-build -b html . ../web/web/static/docs/
```

### Quelques commandes django


