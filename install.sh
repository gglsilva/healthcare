# Create and activate virtual env
virtualenv -p python3 .venv;
. .venv/bin/activate;
# Install requirements
pip3 install -r requirements.txt;
# Install hook pre-commit
pre-commit install;
# Create .env 
python contrib/env_gen.py
# Active .venv and run project
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000