#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install heroku-container-registry
docker login -e _ -u _ --password='303effeb-fe4e-47f1-b712-c1fcd96f5d14' registry.heroku.com
heroku container:push web --app 'intense-mesa-75551'
