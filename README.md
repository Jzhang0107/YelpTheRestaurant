# YelpTheRestaurant
Deliverables
We would like for you to build a web application using Yelp's Fusion API that will help users pick a restaurant or experience.  We want to see your creativity in action! Just make sure your solutions include these requirements:

Submit a deployed web application and include both your website URL and the supporting Github repository.
The app must use Yelp's Fusion API
Your app should be able to plot merchants on a map
Your app should be able to obtain user location via HTML5 Geolocation

# Website URL
https://yelprestaurantpicker.herokuapp.com/

# Front-End
. Boot-strap with html, css, and js
. Leaflet API for mapping coordinates and plotting merchants
. HTML5 geolocation for obtaining user current location

# Back-end
. Flask with python
. Used Yelp's business search API to do most of my requests

# Features Implemented
. Website is deployed
. HTML5 geolocation works
. Yelp's API used
. Leaflet to plot merchants on a map

# How the website functions
Onload of the website, the user is asked to allow their location in order for the geolocation to work. Once allowed, the user can choose from one of four experiences, breakfast, lunch, dinner, or cafes via a multiple choice form. 
After the user selects one, the user's selection along with the users latitude and longitude(obtained from geolocation) is sent to the Flask server with the latitude and longitude being hidden fields.
Depending on what is chosen from the form, the top 5 options for that specific option is displayed and plotted on a map with a picture, name(hyperlink to that restaurant's yelp page), and address.
If none of the options are liked or prefer, the user has the option to search based on more specific criterias such as type of food, desired location, and price range(1-4 based on Yelp's $), and the top 5 results from that is displayed and plotted.
THe top navigation bar gives access back to the mainpage or the github.

# Challenges
. It was my first time fully implementing APIs combined with data from the front-end, it took a while to clean up the API result and playing around with its values to get exactly what I want
. Yelp's business search api returns the names in such a way that if trying to use a for loop to print the names onto the map labels, it creates an error because instead of the apostrophes(') being printed, their ascii equivalent is printed which causes error
. Deploying on Heroku took arguably the longest, trying to figure out environment variables was definitely a learning experience. Learning to deploy on Heroku alone took almost as much time as it did actually making the web app
