#!/bin/bash

cd ~

# copy in the .env file - this file is manually created and placed in this EC2 instance
echo "Copy .env file"
cp .FinkelsteinLab.env ArsenyLabWorkflow/docker/standard_worker/.env

# build and start the container
cd ArsenyLabWorkflow/docker/standard_worker/dist/debian

echo "Build Docker image"
docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml build --no-cache

echo "Start the Docker container"
docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml up

echo "Stop the EC2 instance"
sudo shutdown now