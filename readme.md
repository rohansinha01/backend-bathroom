- Project Name: People Be Poopin 
- Description: Database of the cleanest, most convenient places to go to the bathroom 
- Developers: Rohan Sinha 
- Live Website: https://backend-bathroom-1.onrender.com/restrooms/ 
- Repo: https://github.com/rohansinha01/backend-bathroom 

## Overview

People Be Poopin'. People Be needing to know where to go to the bathroom. People Be wanting a clean place to relieve themselves. People Be wanting to know if they have to buy something to use the bathroom. People Be needing to know where to go to the bathroom. People. Be. Poopin'.

For the backend, I will have a data model that will track the name of the location, location, cleanliness rating, and whether the location requires a purchase. Users will be able to add, update, delete, and show each location. 

## Tech Used
- asgiref==3.8.1
- dj-database-url==2.1.
- Django==5.0.3
- django-cors-headers==4.3.1
- django-environ==0.11.2
- djangorestframework==3.15.1
- gunicorn==21.2.0
- packaging==24.0
- psycopg2-binary==2.9.9
- sqlparse==0.4.4
- typing_extensions==4.10.0
- tzdata==2024.1

## Backend Route Map

| Route Name | Endpoint | Method | Description |
|------------|----------|--------|-------------|
| Restroom Index | /    | GET    | Renders all of the restrooms on a page |
| New Restroom Form | /   | GET    | a form to add a new restrooms |
| Create Restroom | /    | POST    | Creates the new restroom from the form |
| Edit Restroom Form | /restrooms/:id    | GET    | Renders a form to edit an existing restrooms |
| Update Restroom | /restrooms/:id   | PUT    | Updates the existing restroom from the form  |
| Remove Restroom | /restrooms/:id   | DELETE    | Deletes the restroom selected |
| Show Restoroom | /restrooms/:id    | GET    | Renders a detailed page of the restroom |

## ERD (Entity Relationship Diagram)

![Entity Relationship Diagram](https://imgur.com/ZFDAT9L.png)