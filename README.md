# boilerplate

## Create virtual env
- virtualenv .venv

## Activate .venv
- souce .venv/bin/activate

## install requirements
- pip install -r requirements.txt

## Install the git hook scripts
- pre-commit install

## create .env
- python contrib/env_gen.py

## Runserver
- python manage.py runserver

## Create apps
- mkdir ./apps/appname
- python manage.py startapp appname ./apps/appname

# Create virtual environment and install dependencies.
- Run install.sh
    > ./install.sh
- Permission to execute the file
    > chmod +x instal.sh

