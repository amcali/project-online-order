# Sofia's Pizza

Sofia's Pizza is a fictional delivery business in Singapore, that delivers their homemade pizzas to any doorstep in Singapore. They focus on having an online platform to open a means to customers to be able to place orders with itemvia their website. Due to being a small enterprise, Sofia's Pizza only caters to delivery within in Singapore.

This project resembles Sofia's Pizza's online website which serves as their commercial platform to allow users to make and pay for orders online. The link to the website is available [here.](https://sofias-pizza.herokuapp.com)


 
## UX

Aside from creating an online presence for the business, the website also allows users to place orders and pay online for them on the condition of having an account. Anyone without an account is eligible to register for one, provided that a unique username and an unregistered email address is used to create the account. Subsequently for users who have an account and are logged in, pages that require user login authorisation will be uniqely available to them.

A wireframe of the website may be found [here,](https://github.com/amcali/project-online-order/blob/master/Sofias%20Pizza%20-%20Wireframe.pdf) and a diagram of the models created and used to build the website may be found [here.](https://github.com/amcali/project-online-order/blob/master/Sofias%20Pizza%20-%20Django%20Model%20Diagram.pdf)


#### 1) Without account login authorisation
The following will outline the UX for an unregistered user or a user who has not logged into their account, and the pages that are available to them.

__Webpages:__
  * [Home Page](https://sofias-pizza.herokuapp.com/home) - This is interchangeably referred to as the Landing Page, which comprises of a carousel of images and simple content with the intention of using instant visual insight to what is Sofia's Pizza.
  * [Register](https://sofias-pizza.herokuapp.com/account/register) - This is to sign up for a new account.
  * [Login](https://sofias-pizza.herokuapp.com/account/login) - This is for registered users to login to their account.
  * [About](https://sofias-pizza.herokuapp.com/home/about_us) - This page explains what Sofia's Pizza is about and their contact details; and outlines the procedure on how to order.
  * [Menu](https://sofias-pizza.herokuapp.com/menu) - This page lists the menu items which Sofia's Pizza is selling for their delivery service.

__UX Scenarios:__
  1) As a user who wishes to know about the website, one would click the About link in the navigation bar access the About Page, where an overview of Sofia's Pizza business nature may be found.
  2) As a user who would like to order, one would click the Menu link in the navigation bar to access the About Page, where there is instructions on how to order.
  3) As a user who would like to know what Sofia's Pizza sells, one would click the Menu link in the navigation bar to access the Menu Page, where the food items which Sofia's Pizza is selling may be found.
  4) As a user who wishes to start ordering, one may click on the Register link in the navigation bar to create an account which is required in order to start ordering. One may refer to the About Page if in need of instructions on how to order.
  5) As a user with any enquiries, one may refer to the contact details provided in the About Page.



#### 2) With User Login Access Authorisation
The following will outline the webpages which a logged in user is authorised to view upon login, and their respective UX available.


__Webpages:__
  * Home Page - This represents the landing page and is visually the same as that for a user who is not logged in.
  * Menu - Under the mode that a user is logged in, this page will act as a 'shop' page, whereby the items displayed will have an 'add to cart' feature available to them to do their ordering.
  * Cart - Displays all items in the user's shopping cart.
  * Order History - Displays the user's history of orders for which payment was successful.
  * Logout - Allows the user to logout of their account, and redirects to the landing page.


__UX Scenarios:__
   1) Making and Paying for an order
      * i) As a user who wishes to order, one would click the Login link in the navigation bar to login to their account first.     
      * ii) Upon successful login, one would then be directed to the Menu Page, where the option to immediately add items to shopping cart is available.
      * iii) After using the '+' and '-' to add the specific items to the shopping cart, one would then click on the 'Cart' link in the navigation bar to access the Cart Page and view the items and their quantities prior to checkout.
      * iv) Once items in shopping cart are ready to be paid for, one would then click the 'checkout' button to view the total amount due. 
      * v) One would then click the 'Pay' button to then complete the form with the required payment details, and then click the 'submit payment' button.
      * vi) Upon successful payment, one would then be alerted with a message that their payment has been submitted, and subsequently be directed to a 'Payment Successful' page.


   2) Viewing Orders
      * As a user who wishes to review all orders paid for, one would click the 'Order History' link in the navgation bar.


   3) Logout
      * As a use who wishes to logout of their account, one would click the 'Logout' link in the navigation bar, which would direct them to the landing page, and simultaneously be notified that have have successfully logged out.




## Features


### Existing Features

- The following features are available on the website:

- User Registration - This allows a new user to create an account, which requires creating a unique non-existent username, registering a non-existing email address and password.
- Account login - This allows an existing user to login to their account.
- Menu Ordering - This allows the user to view the menu items which Sofia's Pizza sells. For users that are logged into their account, there is an add/remove feature on this page which enables the logged in user to add the items to their shopping cart.
- View Cart - This allows the user to view the menu items and their added quantities into their shopping cart.
- Checkout - This enables the user to proceed to checkout their shopping cart items, so long as the cart is not empty. On this page, the user has an option to clear any menu items from their shopping cart before proceeding to checkout.
- Payment - This enables the user to make payment, which is managed by stripe.
- Payment History - Upon successful payment, the user will view their paid transactions on this page.
- Logout - This page enables logged in users to log out of their account.


### Features Left to Implement
- Reset password - This is to enable registered users to reset their password in the event they may have forgotten it, or wish to amend it.
- Displaying 'cart is empty' on cart page if there are no items in the shopping cart.
- Close down account - This enables users who do not wish to have an active account to close it.
- Favourites list - This would enable users to be able to immediately add their favourite choices of menu items, or a history order to be immediately recalled by the user and re-ordered. This function will assist customers who have their usual order to save the time they would take to create their shopping cart from start.
- Create a timing validator as to when the user is eligible to place an order, which relies on the operation hours of Sofia's Pizza.
- To improve the Menu model in automatically converting price input of menu items. All menu item prices are entered in cents.




## Technologies Used

- AWS Cloud9
- HTML
- CSS
- Bootstrap
- Django
- JQuery
- Postgres
- AWS S3
- Stripe
- Github
- Heroku




## Testing

Manual testing was conducted, for which the scenarios may be found [here.](https://github.com/amcali/project-online-order/blob/master/Sofias%20Pizza%20-%20Test%20Cases.pdf)

The website has been tested to work on mobile responsive devices.




## Deployment


Documentation of the code for this project can be found on GitHub via this [repository.](https://github.com/amcali/project-online-order)
Static and media files used for this project have been stored onto AWS S3 Bucket.
Postgres has been used to store all data.

The project was created on AWS Cloud9, and from which had been deployed onto Heroku via the following BASH CLI:

   `sudo install heroku --classic`
   
   `sudo apt install libpq-dev python3-dev`
   
   `sudo pip3 install gunicorn`
   
   `heroku create sofias-pizza`
   
   `heroku addons:create heroku-postgresql`
   
   `sudo pip3 install dj_database_url`
   
   `python3 manage.py migrate`

Heroku Config Vars: 

   `AWS_ACCESS_KEY_ID`
   
   `AWS_SECRET_ACCESS_KEY`
   
   `STRIPE_PUBLISHABLE_KEY`
   
   `STRIPE_SECRET_KEY`

Update requirements.txt and create Procfile for the purpose of deploying the project to Heroku.

Once deployment on heroku is done, a superuser was created on heroku which acts as the admin account.

Via the superuser account, the menu items were created.


In order to run the code locally, the project may be downloaded from the [GitHub repository.](http://github.com/amcali/project-online-order)
Django will need to be installed on the local environment in order for the project to run, and the following keys need to be implemented in the `.bashrc` file for setup of AWS S3 Bucket and Stripe:

   `AWS_ACCESS_KEY_ID`
   `AWS_SECRET_ACCESS_KEY`
   `STRIPE_PUBLISHABLE_KEY`
   `STRIPE_SECRET_KEY`

After setup, a superuser needs to be created, via which the menu items have to be created in order for any items to become available for a user to be able to view and have during account login for purchasing and paying for items.




## Credits

### Content
- The text content on the [About Page](https://sofias-pizza.herokuapp.com/home/about_us) was sourced from [Pastamania](https://www.pastamania.com.sg)

### Media
- Photos used for the [Landing Page](https://sofias-pizza.herokuapp.com/home) are from [Pexels](https://www.pexels.com)
- Photos used for the [Menu Page](https://sofias-pizza.herokuapp.com/menu) are from [Pastamania](https://www.pastamania.com.sg)

### Acknowledgements

- I received inspiration for this project from the following websites:

   * [Pastamania](https://www.pastamania.com.sg) 
   * [Lieferando.de](https://www.lieferando.de/en/sofias-hamburg)

__All materials and content in this project are solely for educational purposes.__

