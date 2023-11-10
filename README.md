# Codewars App

## System Requirements
This applications requires installations of Python3.11.4, npm, and postgres. The individual packages to be installed are listed in the requirements.txt and package.json files.

Alternatively, running this application in Docker will download all the necessary dependencies within the docker container, requiring no local installations.

## Design Decisions
- React was decided to be used for the frontend application because of it's swift ability to manage changes to the DOM.
- Flask was used for the backend applications becuase of it's lightweight requirements. Given the simplicity of the application, the lightweight feature of Flask was sufficient.
- RabbitMq was used for the messaging service between the backend applications.
- A SQL Postgres database was decided upon because of the structured data that was expected.

## About
This app starts with an HTTP request from the display app. A user can enter their codewars username and will be returned with a list of coding languages that they use on the codewars platform, as well as, their score for each language.

The app makes use of a React frontend, a Flask backend, and a

## Instructions
The app is completely containerized in Docker. To create the relevant images and run the app in Docker, you first need to have docker installed locally. Then you can run `docker compose up` from the project root.

Docker will spin up each application instance, the postgres db, and the rabbit mq message broker.

## Usage
Once the services are up and running in Docker, you can go to localhost:3000 to access the React **display** app. From there, input your codewars username if you have one. You can use mine "sallyman128" as an example if you'd like. The **display** app will send a request to the **analyzer** app. 

The **analyzer** app will fetch the data from the codewars API, do some data cleaning and analysis, and then return a response to the **display** app.

The **analyzer** app will also publish a task to the rabbit mq broker that will be consumed by the **database** app.

The **database** app will take the task from analyzer that consist of an event. And it will save the event to the postgres database.

You can access the docker postgres db from the CLI using the following command in the root director. `docker exec -it postgres-container-ID psql -U usr -d codewars_db`. Just enter the postgres-container-id. You can find this by running: `docker ps`.