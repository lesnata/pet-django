## Table of contents
* [General info](#general-info)
* [Live website](#live-website)
* [Brief description](#brief-description)
* [Technologies](#technologies)
* [Style conventions](#style-conventions)

# General info
Natalie's pet project: Django shop
This repository contains Lesna pet project with Django e-commerce shop

## Live website
Please refer to this link for checking web-site live:
https://django-ecom-live.herokuapp.com/

## Brief description
User can purchase both physical and e-products with guest and existing user 
checkout features. 

Physical products enable the functionality of shipping address block, with help of 
JS "hidden" classes. However, when purchasing e-products only (like 'Project Source Code'),
only user info and payment blocks will be prompted.

Guest functionality is working mainly via JS, please refer to cart.js in static folder.
Registered user functionality pulls out the data directly from DB.

Paypal integration is enabled, but Paypal sandbox business account is used, 
so don't get scarred finish the transaction (of course with previously created 
Paypal sandbox user).


## Technologies
* Django==3.1.4;
* flake8==3.8.4;
* Pillow==8.0.1;
* psycopg2-binary==2.8.6;
* selenium==3.141.0;
* whitenoise==5.2.0
* JavaScript;
* Bootstrap;
* Paypal integration;
* Amazon RDS;


## Style conventions
For code conventions used Flake8 library