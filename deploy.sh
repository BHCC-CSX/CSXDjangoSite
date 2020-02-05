cd mysite/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input


gsutil rsync -R static/ gs://bhcc-csx.appspot.com/static
gcloud app deploy --quiet
