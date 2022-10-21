# DJ_cloud
DJ on cloud


# Installation and deployment instruction

1. Connect to the compute server to deploy this codebase for analysis
2. Navigate to your working directory (e.g. `home` directory)
   
    > cd ~

3. Clone the code repository, and navigate to the root project directory
    
    > git clone https://github.com/ArsenyFinkelsteinLab/DJ_cloud.git
   
    > cd ./DJ_cloud
   
4. Configure a `.env` file - an example env file is provided, see `./docker/standard_worker/example.env`. Users need to make a copy of this file, rename to `.env`, and place in the same directory as the `example.env`, and then fill in the missing values to some of the variables - intentionally left blank (e.g. DJ_USER, DJ_PASS, etc.)  

5. Navigate to the docker subdirectory

    > cd ./docker/standard_worker/dist/debian

6. Build the docker image

    > docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml build --no-cache
   
7. Launch the docker container

    > docker compose --env-file=../../.env  -f docker-compose-standard_worker.yaml up -d