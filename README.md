# Sofia's Pizza

Sofia's Pizza is a fictional delivery business in Singapore, that delivers their homemade pizzas to any doorstep in Singapore. They focus on having an online platform to open a means to customers to be able to place orders with itemvia their website. Due to being a small enterprise, Sofia's Pizza only caters to delivery within in Singapore.

This project is the representation of Sofia's Pizza's online website acting as their commercial platform to enable users to order from them and pay for their orders online. The link to the website is available [here](https://https://sofias-pizza.herokuapp.com)
 
## UX

Aside from creating an online presence for the business, the website also allows users to place orders and pay online for them on the basis of having an account. Anyone who does not have an account is able to register for one, provided that they create a unique username, and an email address that has not been used before.

A wireframe of the website may be found [here.](https://github.com/amcali/project-online-order/blob/master/Sofias%20Pizza%20-%20Wireframe.pdf)
A diagram of the models upon which the website is constructed from can be found [here.]()

This website is for consumers who are wishing for a slice of homemade pizza, and at the convenience of having it delivered to wherever they are in Singapore. To customise to each user's expierience, the website has been set up to require the user to have an account in order to place an order.

Initially upon the [landing page](https://sofias-restaurant.herokuapp.com/home), the content aims to give simple yet quick insight to the user as to what the website is about. Further information about the website and its features are provided in the about page.
Users who have an account and are authorised upon login will have access to different pages.

An unregistered user or a user who is not logged into their account will have access to the following pages:

Home Page - This represents the landing page
Register - This is to sign up for a new account
Login - This is for registered users to login to their account
About - This explains what the website is about, and outlines the procedure on how to order
Menu - This gives a list of the menu items which Sofia's Pizza is selling for their delivery service

The following scenarios address the types of options available to an unregistered user:
1) As a user who wishes to know about the website, one would click the About link in the navigation bar access the About Page, where an overview of Sofia's Pizza business nature may be found.
2) As a user who would like to order, one would click the Menu link in the navigation bar to access the About Page, where there is instructions on how to order.
3) As a user who would like to know what Sofia's Pizza sells, one would click the Menu link in the navigation bar to access the Menu Page, where the food items which Sofia's Pizza is selling may be found.
4) As a user who wishes to start ordering, one may click on the Register link in the navigation bar to create an account which is required in order to start ordering. One may refer to the About Page if in need of instructions on how to order.
5) As a user with any enquiries, one may refer to the contact details provided in the About Page.


A logged in user will have access to the following pages accessible:
Home Page - This represents the landing page and is visually the same as that for a user who is not logged in.
Menu - Under the mode that a user is logged in, this page will act as a 'shop' page, whereby the items displayed will have an 'add to cart' feature available to them to do their ordering.
Cart - Displays all items in the user's shopping cart.
Order History - Displays the user's history of orders for which payment was successful.
Logout - Allows the user to logout of their account, and redirects to the landing page.


## Features


### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

- The following features are available on the website:

- User Registration - This allows a new user to create an account, which requires creating a unique non-existent username, registering a non-existing email address and password.
- Account login - This allows an existing user to login to their account.
- Menu Ordering - This allows the user to view the menu items which Sofia's Pizza sells. For users that are logged into their account, there is an add/remove feature on this page which enables the logged in user to add the items to their shopping cart.
- View Cart - This allows the user to view the menu items and their added quantities into their shopping cart.
- Checkout - This enables the user to proceed to checkout their shopping cart items, so long as the cart is not empty. On this page, the user has an option to clear any menu items from their shopping cart before proceeding to checkout.
- Payment - This enables the user to make payment, which is managed by stripe.
- Payment History - Upon successful payment, the user will view their paid transactions on this page.
- Logout - This page enables logged in users to log out of their account.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Reset password - This is to enable registered users to reset their password in the event they may have forgotten it, or wish to amend it.
- Displaying 'cart is empty' on cart page if there are no items in the shopping cart.
- Close down account - This enables users who do not wish to have an active account to close it.
- Favourites list - This would enable users to be able to immediately add their favourite choices of menu items, or a history order to be immediately recalled by the user and re-ordered. This function will assist customers who have their usual order to save the time they would take to create their shopping cart from start.
- Create a timing validator as to when the user is eligible to place an order, which relies on the operation hours of Sofia's Pizza.



## Technologies Used

_In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- AWS Cloud9
- HTML
- CSS
- Bootstrap
- Django
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- Postgres
- AWS S3
- Stripe
- Github
- Heroku


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment


Documentation of the code for this project can be found on GitHub via this [repository.](https://github.com/amcali/project-online-order)
Static files used for this project have been stored onto AWS S3 Bucket.
Postgres has been used to store all data.

The project was created on AWS Cloud9, and from which had been deployed onto Heroku as follows:

sudo install heroku --classic
sudo apt install libpq-dev python3-dev
sudo pip3 install gunicorn
heroku create sofias-pizza
heroku addons:create heroku-postgresql
sudo pip3 install dj_database_url
python3 manage.py migrate

heroku config: 

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY

Update requirements.txt and create Procfile for the purpose of deploying the project to Heroku.

Once deployment on heroku is done, a superuser is created on heroku.


_This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text in the [About Us](https://sofias-pizza.herokuapp.com/home/about) was sourced from [Pastamania](https://www.pastamania.com.sg)

### Media
- Photos used for the [Landing Page](https://sofias-pizza.herokuapp.com/home) are from [Pexels](https://www.pexels.com)
- Photos used for the [Menu Page](https://sofias-pizza.herokuapp.com/menu) are from [Pastamania](https://www.pastamania.com.sg)

### Acknowledgements

- I received inspiration for this project from the following websites:
[Pastamania](https://www.pastamania.com.sg) 
[Lieferando.de](https://www.lieferando.de/en/sofias-hamburg)

All materials and content in this project are solely for educational purposes.

