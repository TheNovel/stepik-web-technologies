sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf
sudo -s rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart