# 3de3gt Installation

This is a django-rest-framework(backend) and vuejs(frontend) project. It heavily relies on docker and docker-compose, and the reverse-proxy configuration with ssl enabled (more info: https://blog.ssdnodes.com/blog/host-multiple-websites-docker-nginx/ and  https://blog.ssdnodes.com/blog/host-multiple-ssl-websites-docker-nginx/ )

# Requirements

In order to install 3de3gt, you need to install docker and docker-compose in your OS.  For production mode, it is assumed that you configurated your reverse-proxy server according to the links provided above.

# Downloading source
Create the folder where you want to keep your code and run

    $git clone https://github.com/Guatecambia/3de3gt.git


# Running in development

Being on the folder where you located your code run

    $sudo docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

On the backend folder you have all the django project files, and in the frontend folder you have all the vuejs project files.

# Running in production

Please note that your reverse-proxy server should be configured, as well as your DNS configuration.

Use the file docker-compose.prod.secret.yml.template to create your own version of docker-compose.prod.secret.yml.

Fix docker-compose.prod.yml to point to your own URL.

Fix your file: ./backend/gt3de3/settings_secret.py to suit your needs.

Being on the folder where you located your code run:

    $docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.prod.secret.yml up -d

