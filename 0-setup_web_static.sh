#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static.
sudo apt-get -y upgrade
sudo apt-get -y update
sudo apt-get -y install nginx

if [ ! -d "/data" ]; then
	mkdir -p /data
fi

if [ ! -d "/data/web_static" ]; then
	mkdir -p /data/web_static
fi

if [ ! -d "/data/web_static/releases" ]; then
	mkdir -p /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ]; then
	mkdir -p /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
	mkdir -p /data/web_static/releases/test
fi

sudo echo "<html>
  <head>
  </head>
  <body>
	Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
	root   /var/www/html;
	index  index.html index.htm;

        location /hbnb_static {
        alias /data/web_static/current;
	index index.html index.htm;
        }

	location /redirect_me {
        return 301 http://youtube.com/;
    	}

	 error_page 404 /404.html;
    	location /404 {
     	 root /var/www/html;
     	 internal;
    	}

}
" >> /etc/nginx/sites-available/default


sudo service nginx restart
