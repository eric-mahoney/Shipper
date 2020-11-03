# Shipper

## this app is currently not live.

### This project is licensed under the terms of the MIT license.

Open source order management application built in Django. Supports user creation and login. Once logged in users can add new customers, multiple addresses, orders, and order details. 

## Project Status

This project is currently not in development.

Upcoming features planned included:

- deploying to a server for live-demo of application (AWS, Heroku, DigitalOcean, etc.).
- account creation and user login 
- "added by" column to orders to view which employee added which order.
- mark orders for the different levels of completion (not started, in-progress, completed).
- move completed orders to an archive.
- sort orders by date added and filter by completion status.

## Project Screen Shot(s)

<img src="/screenshot/index_screenshot.png" width="600px">

## Installation and Setup Instructions

Clone down this repository. You will need `python3` and `django` installed globally on your machine.  

To Start Server, navigation to ORM application sub-folder and run:

`python3 manage.py runserver`  

To Visit App:

`localhost:8000`  

## Reflection

During the course of this project, I gained proficiency in Django's MTV design pattern by creating and implementing multiple different models, templates, and views. I was also able to gain experience using Bootstrap to create a responsive, flexible web application.

Currently, I have used the following technologies: 

- Django
- Bootstrap
- HTML
- CSS
- JavaScript. 

To create the application, I used Django's "startapp" and "startproject" boilerplates to minimize the amount of setup required.
