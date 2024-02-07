# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Authors
- {{ cookiecutter.author }}

## Initial setup
### 1. Setup the environment variables
The environment variables are in `dev.env` that is used by docker-compose.yml and `prod.env` that is used by `docker-compose.prod.yml`.
Make sure to edit them and change at least the `POSTGRES_PASSWORD` and `DJANGO_SECRET_KEY`

### 2. Build the containers
First you need to install Docker and Docker compose in your machine:
[Install Docker](https://docs.docker.com/engine/install/)
Then build the docker containers. Open your terminal and write:
```bash
$ docker-compose up --build
```
This will run all the build scripts that create the necessary environment for the app to run. Nothing will be installed in your computer. Instead Docker will create containers that run Linux and install all the necessary libraries and dependencies and run the app in there.

### 3. Initialize the app
I have prepared a script called `initapp` that will initialize the app for you. To run it open a new terminal and type:
```bash
$ docker ps
```
This will list all containers that are currently running. We need the `CONTAINER ID` for `app`.
Then type the following (replace `CONTAINER ID` with the id your container has.):
```bash
docker exec -it <CONTAINER ID> ./manage.py initapp
```
This will initialize the database, create tables for caching and create an admin user with whom you can access the admin panel.
> The admin user will be initialized with these credentials:
> username: admin
> password: admin

You can create an admin user with other credentials like so:
```bash
docker exec -it <CONTAINER ID> ./manage.py initapp --username=admin --password=mysuperstrongpassword
```

## Running in production:
### Configure the webserver
Execute the script that will install dummy certificates so that ngix can start:
```bash
chmod +x webserver/scripts/init_letsencrypt.sh
sudo ./webserver/scripts/init_letsencrypt.sh
```

### Building the container
Use the `docker-compose.prod.yml` instead and follow the instructions of step "3. Initialize the app":
```bash
$ docker-compose -f docker-compose.prod.yml up --build
```
