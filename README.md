# Natalie's pet project: Django shop

This repository contains Lesna pet project with Django e-commerce shop

## Live website:
Please check https://django-ecom-live.herokuapp.com/ to chech the code live.

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



## Technology stack 
- Django;
- JavaScript;
- Bootstrap;
- Heroku + Whitenoise;
- Paypal integration;
- SQLite / Postgress;
