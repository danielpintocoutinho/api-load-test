### API Load Test ###

This repository will create a simple REST API using FastAPI to connect with a docker instance of PostgreSQL to stress test and try load balance options


## INSTALLATION ##

Make sure you have a recent Python version (3.10+) and simple run a 
> pip install -r requirements.txt

If you want to use a local instance of Postgres, you can use the docker-compose.yml file. Just make sure you have Docker installed on your machine. Set up a .env file with the password you want to set up in your database. Aditionally you can set up other configurations as shown in the .env.example file, but if not, they have a default value. Then simply run:

> docker compose up -d

## RUNNING ##

As this is a FastAPI application, you can run locally using the following command

> uvicorn app.main:app --reload