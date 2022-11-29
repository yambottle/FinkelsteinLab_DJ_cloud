# ArsenyFinkelsteinLab DataJoint Workflow
ArsenyFinkelsteinLab DataJoint workflow - cloud deployment

# Workflow operation

This workflow is fully containerized using Docker and is currently setup for automatic deployment to AWS EC2 instance that is already provisioned. 
The credentials to access this EC2 instance is set as GitHub secrets (see [GitHub Actions secrets](./github/workflows/start_process.README.md) for details)

Once the required credentials are added, initialization of this workflow is done by manually trigger a predefined GitHub Actions named `start_process` (see code [here](./github/workflows/start_process.yaml))
Your GitHub username needs to be specified in the [***allow-list***](./github/workflows/start_process_allow_list) for you to be able to trigger the GitHub Actions. If you are not in the list yet, make changes to the list and issue a PR for Arseny's approval. 

### How to start a new round of workflow operation

Step 1 - From any browser, navigate to the GitHub [repository for this workflow](https://github.com/ArsenyFinkelsteinLab/DJ_cloud) - make sure to log in to your GitHub account
Step 2 - Click on the ***Actions*** tab, in which you will see the list of available "GitHub workflows" on the left pannel. There is only one for this repo, named `start_process`
Step 3 - Click on the GitHub workflow `start_process`, then on right side, from the dropdown menu "Run Workflow", click the green button "Run Workflow" to trigger one round of operation

### What is the expected behavior?
Once a new round of operation is triggered with the GitHub Actions above, the pre-provisioned EC2 instance will start, and then the following steps are performed
1. Clone this repository - this is recloned everytime the flow is triggered, ensuring the latest version of the code is used
2. Rebuild the Docker image - again, docker image is rebuilt everytime, ensuring latest version of the workflow is deployed
3. Lauch the Docker container with the newly built image - this will then run all of the DataJoint computation, essentially all `.populate()` calls defined [here](https://github.com/ArsenyFinkelsteinLab/DJ_cloud/blob/main/workflow/populate/worker.py#L27)
4. Once finished (successful or not), the Docker container will terminate itself, thus trigger the EC2 instance to shutdown

# Installation and deployment instruction
For installation and deployment on any other resources (e.g. local or other cloud resources), see [local deployment](./docs/local_installation_and_deployment.md)