#!/bin/bash

cd ~

# copy in the .env file - this file is manually created and placed in this EC2 instance
cp .FinkelsteinLab.env ArsenyLabWorkflow/docker/standard_worker/.env

# build and start the container
cd ArsenyLabWorkflow/docker/standard_worker/dist/debian

docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml build --no-cache
docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml up

# stop the EC2 instance
sudo shutdown now