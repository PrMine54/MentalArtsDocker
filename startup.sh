#!/bin/bash

echo "Starting Wordpress"
cd Wordpress
docker-compose up -d
cd ..

echo "Starting SQL"
cd SQL
docker-compose up -d
cd ..

echo "All services started"