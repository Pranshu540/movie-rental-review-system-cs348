# movie-rental-review-system-cs348
The group project GitHub repo for CS348.

Creating and loading the sample database:
Using MySQL
Run the SQL queries from sampledata/createtables.sql to create the test tables
Run the SQL queries from sampledata/populatetables.sql to populate the test tables with data
If you need to drop the tables you can run the SQL you can run the queries from sampledata/droptables.sql

Running the application:
Run main.py

Supported Features:
User Creation and Authentication
	- Users are prompted to login after starting main.py
	- Can create new user or login to existing user
Search Filters:
	- Users can filter out movies from the database
	- Can Filter based on the movie title, genre, and/or rental availability
Rental Transactions:
	- Users can get a list of all rental history
	- Users can pick a movie to rent if they have sufficient funds in their wallet
Review System:
	- Users can create a review for a movie including a rating and comments
	- After creation users can modify or delete their reviews as desired
