release: python manage.py migrate --noinput
web: gunicorn portfolio.wsgi:application --log-file -