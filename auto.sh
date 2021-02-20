#!/bin/sh

git add -A
read COM
git commit -m $COM
git pull --no-edit
echo "git pull completed!"
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
