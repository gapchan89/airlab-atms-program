# airlab-atms-program
Airlab Application Demo code

This repository contains 2 set of codes
1. Application. This is the flask python application of the API. Dockerfile is provided in this folder for creating an docker image for deployment
2. Infra. This is the minikube setup which creates a namespace, deployment with 1 replica, and a service.

Requirements for running infra
1. 2 parameters will need to be defined in the kubernetes key store
1.1. api-key - This is the API key required to query airlab backend
1.2. base_api_url - This is the base API URL e.g. "https://open-atms.airlab.aero/api/v1/"

CICD
Github actions are configured to check if a change is pushed to "main" branch. If a push is detected then the following will happen
1.1. Checkout code from main branch
1.2. Build the image and push into minikube respository - Minikube and docker environment should be running
1.3. Deploy (or update) 

On pull request to qa or prod branch, a similar flow would be done but into target environment. Ideally, it should download from an image respository

Possible Enhancements
1. Depending on the frequency of the changes in data source, it might be better to store data locally. This will allow service to still be useable even if the backend is down. A seperate pod would be setup to query the airlab server periodically and store it in a local DB
2. Depending on the scale of the application, frontend and backend could be split in separate pods. This allows horizontal scaling of the frontend/backend when needed e.g. when more features are added
3. Caching of the results if the data sources does not change frequently e.g. using Azure CDN
4. Test cases in CICD flow to perform basic checks e.g. query sample API and matching responses