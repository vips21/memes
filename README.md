## Internal Codal Project Management System

#### Pre-requisites
    Python 3.7
    sqlite3

#### Installation 
    Create environment with Python 3.7
    python3.7 -m virtualenv MyEnv
    source MyEnv/bin/activate
    cd cato/backend
    pip install -r requirements.txt

### Create super user
    python manage.py createsuperuser

### Run server
    python manage.py runserver    