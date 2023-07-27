# Healty-Food

This is the e-commerce application which is the last project to Code Institute portfolio projects.

Healthy Food is an online order shop where you can buy (order) food online and get delivered to you'r home. Shop offers variety of food which is healthy.
User can choose from vegan frendlly food such as meat free food, also we have food with meat and also healthy portions aswell. On the site there is 
also a review section (forum) where user can leave theyre experience from ordering from us.


## UI/UX

This website doesn't have any flashy features added to it. This is down to the fact that most expected customers will be surfing the site in good speed and not going to be overloaded 
with features that serve no purpose other than being showy. That way custumer can navigate in the site quickly.

## Agile

This project was designed and built using the agile approach. Right from the initial planning through to final development. To help visualise the process I created a GitHub project and utilised the provided Kanban board method to split project elements into user stories and manageable tasks.

## Wireframes

The initial wireframes in Figma are an overly simplified version of the finished product and merely served the purpose of listing most of the site's essential features.
Not all features and functions are covered by these first drafts.

![main-page](/media/main-page-fr.png)

![category](/media/product-category-fr.png)

![product](/media/products-fr.png)

![reviews](/media/reviews-fr.png)

![about](/media/about-fr.png)

![signin-lonin](/media/sign-log-fr.png)

![basket](/media/basket-fr.png)


## Site Goals

This site is the online shop of the Healthy Food. There are few categories that customers can cheese they'r food from and get it delivered to there home.
It'a aiming for the custumer to eat healthyer 
Custumers also can leave theyr review about the food. In the site it says how can costumers can contact to the busines also shows the working hours so 
the costumer can contact if they have any issues with there order or anthing else.

## UX

### Strategy

  User comes here with the interest of the healthy food so the user have selection of the diffrent dishes. An easy way of making a selection from it and a simple 
  payment method along with the process. If the user is not sure about the produtc user can come to the review section to check what other custumers have to say 
  about theyr order experience.

### Scope

  Addresses what functions and features are within the scope of the project. Basic and essential e-commerce functionality was key to this project. This means that most features included are a basic requirement. Features like user sign up and login, user profile creation, checkout functionality and secure online payment had to be implemented, as well as basic CRUD funtionality for authorised users.
(Site owner can easily update and delete the product. New products can also be added. All these features are only accessible to authorised users.(site owner))

### Structure

  Defines how users can navigate the site and utilise all existing features. The structure of the site is modelled on a basic e-commerce application with an additional forum page. The structure allows users to browse products and make purchases as well as visit the review page to find information about other costumer experince.
  Authenticated users can store their personal information in a user profile for the purpose of faster order handling and leave review in the review section.

All CRUD functionality is placed intuitively with the relevant features of the site (individual products, review posts). A super-user can avail of the same navigation options as as any authenticated users. However, these include additional features limited to authorised users.

### Skeleton

  Puts features defined in structure into navigational elements. For a first outline of the project skeleton see Wireframes. To guarantee intuitive navigation of the site, both the navbar and the main content follow a standard layout pattern that should be familiar to most users. The navbar provides links to the main features and functions of the site, varying based on whether a user is authenticated or not. On small to medium screen sizes a drop-down menu takes the place of the full navbar. The shopping basket link in the navbar is being updated everytime a user adds an item (of a differnt type!) to the basket. A footer with social media links.

# Features

### Existing Features

## Navigation

* Responsive navbar with dropdown menu
* Navigation options dependant of user authentication/authorisation

## Home page

* Home page with banner image and introduction
* Order Now button 

## About page

* Contact info incl. address, phone number and email
* Shop opening hours
* Info about Healthy food

## Sign Up

* Allows new users to create account
* Sign up process includes confirmation email with confirmation link

## Login

* Allows existing users to log into their account
* Includes Remember me checkbox and Forgot Password option

## Logout

* Allows authenticated users to securely log out of their account

## Category page

* Lists all categories of products

## Products page (of same category)

* Lists all products of the same category
* Quick link to category page

## Product details page

* Product image, description and price
* Quick link to respective category
* Quantity input
* Continue Shopping button ("Browse more")
* Add to basket button
* Edit and delete option for authorised users for each product

## Add Product page

* Authorised admin users only!
* Complete product form with image upload option
* Cancel button
* Add product button to add product to database

## Edit Product page

* Authorised admin users only!
* Complete product form with image upload option
* Form is pre-populated with existing product's details
* Cancel button
* Update product button to update existing product in database

## Delete Product option

* Authorised admin users only!
* Option on product details page
* Delete button to delete existing product from database

## Reviews Page

* Gives option to select the title to which product you want to give review
* Shows creatted date review owner can delete or edit it

## Shopping Basket

* Live update of basket status in navbar
* Counter in nav element displays only the number of different products, not the total of all products.

## Shopping Basket

*  View of currently selected products and their quantity
*  Quantity adjustment option
*  Product removal option
*  Display delivery cost (currently always 0) and grand total
*  Continue shopping button
*  Proceed to checkout option

## Checkout page

* Checkout form, including sections for personal info, contact details and card details
* Option to save details to profile for authenticated users
* Current order summery
* Edit Basket button
* Pay now button

## Checkout Success page

* Confirms successfull order and informs user that email was sent to the address specified
* Displays order details, contact and billing info
* Continue Shopping button ("Back to products")

## Profile

* Contact address form (pre-populated if user has previously saved his info)
* Update Info button
* Listing of past orders in order history

## Possible Future Features

### Extended product range

The shop has the potential to extend its product range by categories and even products so the user would have more options to choose from.

### Search option

Add search option so the user could find food by puting it in the search bar.Currently the product selection is so small that a search bar was deemed unnecessary but would make sense to implement along with an extended product range.
Leaving comment on the other people reviews.

# Technologies Used

## Work Environments and Hosting

* Figma (Wireframes)
* GitHub (Version control)
* GitPod (IDE)
* Heroku (Site hosting)
* AWS - Amazon Web servises (S3) (Hosting static and media files)

## Python Libraries

* Gunicorn (Python HTTP server for WSGI applications)
* boto3 (integrates python libraries with AWS services)
* django-storages (collection of custom storage backends for Django)
* Flake8 (Python linter used for python code validation)

## Django Libraries

* django-allauth (User authentication)
* django-crispy-forms (Control rendering behaviour of Django forms)
* Bootstrap5 template pack for django-crispy-forms

## Payment processing

* Stripe (Online payment platform)

## Emails/Newsletter

* Gmail (Real email sending)
* Mailchimp (Automated newsletter subscription service)

