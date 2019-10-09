## Django-Order-Form-App

An application used to store user information in a SQLlite database for easy retrieval. This application could be use by a local store to keep on track of orders and manage their progress.

## Project Status

This project is currently in development. Users can add new customers, multiple addresses, orders, and order details. Upcoming features planned include:

- deploying to a server for live-demo of application (AWS, Heroku, DigitalOcean, etc.).
- account creation and user login 
- "added by" column to orders to view which employee added which order.
- mark orders for the different levels of completion (not started, in-progress, completed).
- move completed orders to an archive.
- sort orders by date added and filter by completion status.

## Project Screen Shot(s)

![screenshot](/screenshot/index_screenshot.png)

## Installation and Setup Instructions

Clone down this repository. You will need `python3` and `django` installed globally on your machine.  

To Start Server, navigation to ORM application sub-folder and run:

`python3 manage.py runserver`  

To Visit App:

`localhost:8000`  

## Reflection

This is a week long project for my IT-409 (Django Web Development) class. All of the requirements for the project's models and implementations were given to me to as part of the project requirements.

During the course of this project, I gained proficiency in Django's MTV architecture by creating and implementing multiple different models, templates, and views. I also was able to gain experience using Bootstrap to create a responsive, flexible web application.

Currently, I have used the following technologies: Django, HTML, CSS, Bootstrap, and JavaScript. To start the application, I used Django's "startapp" and "startproject" boilerplates to minimize the amount of setup required.
