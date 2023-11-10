# Django + Docker Boilerplate
After having to initiate multiple Django projects (all having more or less the same setup) I decided to create this boilerplate with the most common setup and services that I use for my projects.

So this is a complete dockerized project that is orchestrated by docker-compose that also includes some extra services such as Postgres and Redis and can be used as a base for many use cases.

I hope other people find it useful as well. If you do feel free to contribute.

## What's incuded?
-   Django 4.2
-   django-extensions
-   django-json-widget
-   django-constance
-   requests
-   As services:
    -   Postgres
    -   Redis

## Initial setup
### 1. Create a new project with coockiecutter
Install cookiecutter:
```bash
pip install cookiecutter
```
Then start the project:
```bash
cookiecutter https://github.com/AGTGreg/DjangoBoilerplate/tree/coockiecutter
```
You will be prompted to answer some questions to customize the project.

### 2. Setup the environment variables
The environment variables are in `dev.env` that is used by docker-compose.yml and `prod.env` that is used by `docker-compose.prod.yml`.
Make sure to edit them and change at least the `POSTGRES_PASSWORD` and `DJANGO_SECRET_KEY`

### 3. Build the containers
First you need to install Docker and Docker compose in your machine:
[Install Docker](https://docs.docker.com/engine/install/)
Then build the docker containers. Open your terminal and write:
```bash
$ docker-compose up --build
```
This will run all the build scripts that create the necessary environment for the app to run. Nothing will be installed in your computer. Instead Docker will create containers that run Linux and install all the necessary libraries and dependencies and run the app in there.

### 4. Initialize the app
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
chmod +x webserver/scripts/init-letsencrypt.sh
sudo ./webserver/scripts/init-letsencrypt.sh
```

### Building the container
Use the `docker-compose.prod.yml` instead and follow the instructions of step "3. Initialize the app":
```bash
$ docker-compose -f docker-compose.prod.yml up --build
```

## Special thanks
I would like to thank:
- [Philipp](https://github.com/wmnnd) For the `init-letsencrypt` script and for his awesome instructions on setting up nginx and certbot.