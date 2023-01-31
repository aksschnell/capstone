### Project description

This project is the final project submitted in the CS50W course from Harvard University

My project is a website where users can browse different movies based on different parameters. For example by genre, by rating and by release year. 

It's even possible to search for the different movies' titles and then apply the filter to those as mentioned above. 

It’s also possible to post reviews if you’re logged in. The user's review counts towards the average rating of the movie that is being reviewed. 
Other users can like or dislike the reviews if they agree or disagree and so on. 
Every user has their own page where all their reviews are displayed, on each of these pages the users total number of reviews is displayed as well as their average rating of all their movie reviews. When the user clicks on a specific review on the userprofile page they are redirected to the specific movie they clicked on. 

### Distinctiveness and Complexity

The website is distinctive since it builds on an idea that hasn't been explored previously in the CS50 course, that being the movie browser concept which comes with it's own set of challenges. It has unique features and it utilizes new models.

The new features being those mentioned above, the ability to search by title, filter by genre, rating and release year etc.

The most complex part of the project being the code that is responsible for filtering which movies that are shown to the user depending on what parameters that have been applied using the filtration feature. 

When the list of movies has been filtered, the list gets paginated which means that a maximum of 9 movies is shown per page. The user can navigate through the different pages with the Next & previous buttons at the bottom of the page. 

The different movies are situated insert their own bootstrap row div which makes them act as rows which ensures the movies are shown site by site, and not on top of one another

As well as the code that inserts a new review into the database which is done via a post method. The different post methods have security features that ensure that a user can't post two reviews on the same movie or mark a review as disliked twice and so on.

When a user marks a post as disliked or liked the page doesn't get refreshed since the frontend updates with the help of JavaScript, as expected not only the frontend gets updated but the database as well, using a post method. This means that what is shown to the user always represents the database. In other words, when a given page is refreshed it doesnt change the frontend. 

### How to run the application

Like any other django project, the application is run by using the djangs build in local server hosting by typing "python manage.py runserver" in the terminal.

You are welcome to register a user to get access to all the features of the website (reacting to other peoples review, posting a review of your own and so on)

### Files

#### index.html

In this file all the html and in html python code responsible for the frontpage is situated.

The file contains the code that shows the different buttons that the user can press in order to filtrate the visible movies. In the "sort-by" div we see the different buttons as mentioned above. The different buttons' colors are changed depending on whether the filter associated with the buttons has been applied or not. 

The dropdown list that holds all the available genres gets dynamically updated should a new genre be added to the database

in the "row" div each of the movies are being displayed with their appropriate information such as title, genre and so on. It's also here the code responsible for making sure that bootstraps 12 columns system is being utilized. In this case each movie takes up 4/12 of the area.

The footer is where the next and previous buttons are contained which functions with the help of the pagination feature as mentioned earlier.
The code that is responsible for pagination is not in this file and will be explained in another file

#### index.js

Most of the code in this file are functions that gets fired on different button clicks. The functions all change the different url parameters that the index method in view.py uses in order to determine which filters have been applied.


#### layout.html

Most of the html code in this file is something we have seen previously but it's in this file where the html responsible for the search field is situated. Before the search filed can be shown, whether the user is on the index gets checked on line 52. I do this to make sure that users can only search on the index page which is the only page where the search function is functional.

#### login.html, register.html

These files are self explanatory since the way login and register features work is the same we have seen in previous projects in this course.

#### movie.html

In this file we have the code responsible for showing the specific movie that the user has clicked on. This means that when a user clicks on a movie on the index page, the user gets taken to the associated movie page, which this file is the template for.

The different html elements' innerHTMl is empty initially but gets filled with the right information with the help of the movie.js file

It's not only the movie's information that is displayed in this template but also the associated reviews which once again utilizes bootstraps 12 rows system. The different reviews associated information is obviously also displayed. When clicking on the the username of the review poster the user gets taken to their profile page

If the user hasn't posted a review on the current movie that is shown, it gets displayed to the user, so that they can post a review, with a description and rating, as mentioned earlier this rating counts towards the average rating of the movie.


#### movie.js

As mentioned above the movie.html gets changed with the right movie information with the help of the code in movie.js

This is done with a get request to the API movie endpoint. The appropriate html elements' innerHTML is then updated.

As explained in the end of the Distinctiveness and Complexity chapter, the amount of dislikes and likes get updated dynamically in the frontend, and on the movie page, the code responsible for that is situated in this file.

When the user submits a review using the form in the movie.html file it gets processed in this file. The users review is posted with a fetch method and the review API endpoint


#### profile.html

This is the file that is responsible for showing all the users relevant information to the user. This includes the username of the profile, the total number of reviews and the average rating of each of all the reviews the user has posted.

Under the information all the profiles associated reviews are displayed with the bootstrap 12 rows system. Clicking on any of the reviews takes the user to the movie to the appropriate movie page


#### layout.js

In this file the value of the search field gets updated to always reflect the current search parameter.

Also the current search parameter gets updated with the serach.addEventListener function which sets the current search parameter to whatever the user has typed in the search field when Enter is pressed.


#### models.py

In this file all the projects models are located. I have a model for genre, movie, review and reaction who are interconnected with foreignkeys to one another.


#### views.py

In this file most of my python code is located. The most complex of all the views being the index view. 

##### index view

It's in this view that i get all the parameters(filters) and apply the filtration to the list of movies as needed. The most difficult one probably being the search function since it requires a good understanding of loops, arrays and how strings function in Python, and the ability to put them all together.

Other than that the way that the genre and release/rating filtration works is pretty straight forward.

After all the filtration has been applied, the final list of movies gets paginated to only show 9 movies per page. I chose 9 since the index page shows 3 movies side by side which made 9 the ideal number.


##### profile view

Most of the code in this view is pretty simple, for example how the average rating of the user is calculated and so on.

But how the review objects are manipulated in order to be easier read in JavaScript is a bit more complicated. Once again it requires are good understanding of loops but more so how objects function in Python.


#### movie view

Most of the code is something we've seen in the other views. But the only thing that gets feeded to the template is id and already_reviewed variables. The reason being that the movie.html utilizes a JavaScript get function to populate the html elements responsible for showing the specific movie's details.


#### api_movie view

This is a an API endpont that simply returns a movie based on the id that has been provided


#### react view

This is the API endpoint that is responsible for handling all requests associated with posting and deleting reactions.

Both the post and delete sections of this view have features that make sure that the user hasn't already reacted to the specific review, and the user isn’t trying to delete a reaction that doesn't belong to them and so on.

##### urls.py

This file holds all the urls for the project including the API endpoints that the API views uses as explained above.













