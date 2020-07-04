# Deploiement du projet

## Deploiement des packages python from scratch

Depuis le user de developement, création de l'env pipenv:
`pipenv --python /usr/bin/python3`

Ajout des packages python:
```
pipenv install django psycopg2-binary celery django-celery-results scikit-optimize cx-oracle
pipenv install nose pylint --dev
```

## Deploiement des packages python depuis 