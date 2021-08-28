python /app/manage.py collectstatic --noinput
python /app/manage.py migrate

mod_wsgi-express start-server osg-support.wsgi --user www-data --group www-data

# gunicorn osg-support.wsgi -b 0.0.0.0:8000 --timeout 900 --chdir=/app --log-level debug --log-file -
