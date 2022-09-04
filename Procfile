web: gunicorn base.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic