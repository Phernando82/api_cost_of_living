## Title

<h1 align="center"> Unofficial Numbeo API </h1>

## Index

* [Title](#title)
* [Index](#index)
* [Project Description](#project-description)
* [Project Status](#project-status)
* [Project Features](#project-features)
* [Project Access](#project-access)
* [Technologies used](#technologies-used)
* [People-Developers of the Project](#people-developers-of-the-project)

## Project Description

This project uses the Scrapy framework to web crawl the Numbeo page and extract the following information as an example:

`Meal, Inexpensive Restaurant`	

`Meal for 2 People, Mid-range Restaurant, Three-course`

`One-way Ticket (Local Transport)`

`Monthly Pass (Regular Price)`

`Gasoline (1 liter)`

`Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment`

`Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)`	

`Apartment (1 bedroom) in City Centre`

`Apartment (1 bedroom) Outside of Centre`

`Apartment (3 bedrooms) in City Centre`

`Apartment (3 bedrooms) Outside of Centre`

`Average Monthly Net Salary (After Tax)`

The information is saved in a SQLite database and can be retrieved for direct query to the database. Using Flask, routes are created to provide information in JSON format through URLs, thus generating an API that can be consumed to search for this information. This project was hosted on Heroku in order to provide a continuously integrated server, since it is possible to run Scrapy, update the information and then deploy.

## Utility

Used in projects that need information about the cost of living in a given city.


## Project Status
![Badge under development](http://img.shields.io/static/v1?label=STATUS&message=UNDER%20DEVELOPMENT&color=GREEN&style=for-the-badge)

## Project Features

- `Web Scraping`: scans the searched city cost information
- `Storage`: save information in database
- `Flask API`: provides information in JSON file

## Project Access

- `Github`: fork the project
- `Dependencies`: install dependencies from requirements.txt file
- `Database`: run the db_script.py script to generate the database
- `Scan the page`: set the value of the city variable and run the scrapy crawl numbeo command
- `API in service`: run api_numbeo.py file to leave in service
- `Authorization`: via the default url first generate the default_url/login token and set the x-access-token variable
- `Get data`: via the standard url first select the endpoint: /city and then the http verb GET

## Technologies used


  <img align="center" alt="Fer-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">- `Python`
  
  <img align="center" alt="Fer-Pyc" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg" /> - `Pycharm`
  
  <img align="center" alt="Fer-Her" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-original.svg" /> - `Heroku` 
  
  <img align="center" alt="Fer-Flas" height="30" width="40"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" /> - `Flask`
  
  <img align="center" alt="Fer-Vsc" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" /> - `VS Code`
  
  <img align="center" alt="Fer-Sql" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" /> - `SQLite`

## People-Developers of the Project
[<img src="https://github.com/Phernando82.png?size=460" width=115><br><sub>Fernando</sub>](https://phernando82.github.io/portfolio/index.html) 
##
![Github Issues:](https://img.shields.io/github/issues/Phernando82/api_cost_of_living)
![Github Forks:](https://img.shields.io/github/forks/Phernando82/api_cost_of_living)
![GitHub Org's stars](https://img.shields.io/github/stars/Phernando82/api_cost_of_living)
![Github License:](https://img.shields.io/github/license/Phernando82/api_cost_of_living)

