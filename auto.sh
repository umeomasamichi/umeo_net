#!/bin/sh

git add -A
read COM
git commit -m $COM
git pull --no-edit
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart nginx.service
pkill gunicorn 
gunicorn --bind 127.0.0.1:8000 umeo_net.wsgi -D 
