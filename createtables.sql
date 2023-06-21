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
    pasword VARCHAR(30),
    wallet DECIMAL(7, 2)
);

CREATE TABLE Review (
    uid INT NOT NULL REFERENCES User(userid),
    mid INT NOT NULL REFERENCES Movie(mid),
    review_date DATE, /* 'YYYY-MM-DD' */
    rating INT CHECK(rating BETWEEN 1 and 5), /* Out of 5 stars */
    comment VARCHAR(100),
    PRIMARY KEY(userid, mid)
);

CREATE TABLE Rental (
    uid INT NOT NULL REFERENCES User(userid),
    mid INT NOT NULL REFERENCES Movie(mid),
    rent_date DATE, /* 'YYYY-MM-DD' */
    due_date DATE, /* Standard rent period is 2 weeks */
    is_active INT, /* 1 if rental is currently active, otherwise 0 */
    PRIMARY KEY(userid, mid)
);