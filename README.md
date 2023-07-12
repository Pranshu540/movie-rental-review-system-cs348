# movie-rental-review-system-cs348
## The group project GitHub repo for CS348.

## Creating and loading the sample database: <br />
Using MySQL <br />
Run the SQL queries from sampledata/createtables.sql to create the test tables <br />
Run the SQL queries from sampledata/populatetables.sql to populate the test tables with data <br />

## Generating Production Dataset: <br />
IMDB dataset is retreived directly from its link, we have a Python file to <br />
filter, cleanse and generate production data used by our database. <br />

## Running the application: <br />
Edit .env file to set database information <br />
Run `pip install -r requirements.txt` in the root directory <br />
Run main.py <br />

## Supported Features:
User Creation and Authentication
- Users are prompted to login after starting main.py
- Can create new user or login to existing user

## Search Filters:
- Users can filter out movies from the database
- Can Filter based on the movie title, genre, and/or rental availability

## Rental Transactions:
- Users can get a list of all rental history
- Users can pick a movie to rent if they have sufficient funds in their wallet

## Review System:
- Users can create a review for a movie including a rating and comments
- After creation users can modify or delete their reviews as desired

## User Deletion:
- Users can choose to delete their own account after logging in
- After account deletion all reviews and rentals from the user will be deleted, movie rental quantities will be updated
