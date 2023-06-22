/* Create table statements*/
CREATE TABLE Movie (
    mid INT NOT NULL PRIMARY KEY,
    title VARCHAR(50),
    genre VARCHAR(30),
    release_year INT, /* YYYY */
    duration INT, /* minutes */
    rental_price DECIMAL(5, 2), /* Standard price is $9.99 for now */
    rental_quantity INT
);

CREATE TABLE User (
    uid INT NOT NULL PRIMARY KEY,
    username VARCHAR(30),
    password VARCHAR(30),
    wallet DECIMAL(7, 2)
);

CREATE TABLE Review (
    uid INT NOT NULL REFERENCES User(uid),
    mid INT NOT NULL REFERENCES Movie(mid),
    review_date DATE, /* 'YYYY-MM-DD' */
    rating INT CHECK(rating BETWEEN 1 and 5), /* Out of 5 stars */
    comment VARCHAR(100),
    PRIMARY KEY(uid, mid)
);

CREATE TABLE Rental (
    uid INT NOT NULL REFERENCES User(uid),
    mid INT NOT NULL REFERENCES Movie(mid),
    rent_date DATE, /* 'YYYY-MM-DD' */
    due_date DATE, /* Standard rent period is 2 weeks */
    is_active INT, /* 1 if rental is currently active, otherwise 0 */
    PRIMARY KEY(uid, mid)
);

/* Drop table statements */
DROP TABLE Movie;
DROP TABLE User;
DROP TABLE Review;
DROP TABLE Rental;

/*Insertion statements */
/* Sample Movies */
INSERT INTO Movie VALUES (1, 'The Battle of Trafalgar', 'War', 1911, 51, 9.99, 25);
INSERT INTO Movie VALUES (2, 'Egyptian Cruise: Part 1', 'Comedy', 1986, 60, 9.99, 19);
INSERT INTO Movie VALUES (3, 'The Amazing Spider-Man', 'Sci-Fi', 2012, 136, 9.99, 13);
INSERT INTO Movie VALUES (4, 'The Shawshank Redemption', 'Drama', 1994, 142, 9.99, 16);
INSERT INTO Movie VALUES (5, '2001: A Space Odyssey', 'Sci-Fi', 1968, 149, 9.99, 2);
INSERT INTO Movie VALUES (6, 'The Great Gatsby', 'Romance', 1974, 144, 9.99, 7);
INSERT INTO Movie VALUES (7, 'The Dark Knight', 'Action', 2008, 152, 9.99, 8);
INSERT INTO Movie VALUES (8, 'Harry Potter and the Order of the Phoenix', 'Action', 2007, 138, 9.99, 1);
INSERT INTO Movie VALUES (9, 'Avatar', 'Action', 2009, 162, 9.99, 5);
INSERT INTO Movie VALUES (10, 'The Book Thief', 'Drama', 2013, 131, 9.99, 3);

/* Sample Users */
INSERT INTO User VALUES (1, 'movielover123', 'Secret48!', 500.00);
INSERT INTO User VALUES (2, 'batman', '#Imbatman6', 90000.00);
INSERT INTO User VALUES (3, 'harold', 'Passwordd88%', 5.00);
INSERT INTO User VALUES (4, 'george', '*Captain34', 0.00);
INSERT INTO User VALUES (5, 'grace', 'Swiftie97&', 9.99);

/* Sample Reviews */
INSERT INTO Review VALUES (3, 4, '2017-02-21', 5, 'Masterpiece!');
INSERT INTO Review VALUES (2, 7, '2023-06-16', 5, 'I love this movie, Batman rocks!');
INSERT INTO Review VALUES (2, 3, '2023-06-16', 1, 'Spider-Man is not as as cool as Batman :(');
INSERT INTO Review VALUES (1, 3, '2019-09-08', 4, 'Good, but CGI was a bit over the top.');
INSERT INTO Review VALUES (5, 9, '2015-12-25', 3, 'Decent classic');
INSERT INTO Review VALUES (4, 10, '2023-06-17', 4, 'Teaches people how to steal, great for a broke person like myself');

/* Sample Rentals */
INSERT INTO Rental VALUES (1, 3, '2015-12-20', '2016-01-03', 0);
INSERT INTO Rental VALUES (2, 7, '2023-06-14', '2023-06-28', 1);
INSERT INTO Rental VALUES (2, 3, '2023-06-15', '2023-06-29', 1);
INSERT INTO Rental VALUES (3, 4, '2017-05-02', '2017-02-19', 0);
INSERT INTO Rental VALUES (2, 8, '2023-06-10', '2023-06-24', 1);

