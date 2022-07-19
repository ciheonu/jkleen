release: python manage.py migrate

web: gunicorn jkleen.wsgi