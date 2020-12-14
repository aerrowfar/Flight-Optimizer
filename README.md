# Flight-Optimizer
Flight-Optimizer aims to find the cheapest combination of flights between multiple destinations in a trip given some initial constraints. This web application 
accepts a window of acceptable time to depart for your multi-leg trip, the latest you'd be willing to return, and up to 4 destinations with a minimum and maximum number of days at that location. The intermediate values are stored in a noSQL database, MongoDB. An API is then utilized drawing values back from the database, all possible combinations are calculated, and the most cost effective way of travelling a multi-leg trip returned. 

All files in this web application except api.py is my work. 

This web application is currently in alpha stage, not all bugs are ironed out.


__init__.py : app starts here, sends the application to routes.py
a. we initialize the database
b. we initialize the application

config.py: loaded initially as well
a. declare database
b. declare secret key - I chose to implement this because the secret_key value sets
declared here sets the application up for encryption potential and web security down
the line.

routes.py: main part of the application, I chose to include everything in a centrally and
cohesive manner in the same python file that accesses other python files as needed. This keeps things organized.
a. all page logics are declared here
b. all html files for pages are declared here
c. all html files use flask’s “extends html” feature, this enables me to write html in
reusable objects , it's essentially object oriented html. this prevents a lot of copy
pasting and duplicate code
d. all incoming and outgoing variables are tracked here
e. outbound purchase link is generated here
f. database fetches are coded here

models.py: accessed by routes when it comes to storing data.
a. In here I set up how data is actually stored in the database, routes organizes all
input data for the database

form.py: accessed by routes when it comes to accepting form inputs from the main page.
a. In here, we validate the form data, this means:
  i. Which fields requires an input and which ones don't, here I
  decided to only require input for two destinations so the app can still optimize
  between destinations A and B; C and D if provided.
  ii. Length of inputs is appropriate - it is important to have this check to
  prevent database errors and API errors if a very big input is provided
  maliciously
  iii. Numbers are in an acceptable range - this is important because we want
  our duration of stay, the only integers field, to be in the designed window of time. For example, app is not designed to optimize flights that are years apart.
