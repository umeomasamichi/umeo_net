#!/bin/sh

python manage.py makemigrations
python manage.py migrate
echo "migration completed!"
python manage.py collectstatic --noinput
echo "collect completed!"
sudo systemctl restart nginx.service
echo "nginx restarted!"
pkill gunicorn 
gunicorn --bind 127.0.0.1:8000 umeo_net.wsgi -D
echo "gunicorn restarted!"
