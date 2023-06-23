CREATE TABLE Movie (
    mid INT NOT NULL PRIMARY KEY,
    title VARCHAR(50),
    genre VARCHAR(30),
    release_year INT, /* YYYY */
    duration INT, /* minutes */
    rental_price DECIMAL(5, 2), /* Standard price is $9.99 for now */
    rental_quantity INT
    CONSTRAINT chk_rental_quantity CHECK (rental_quantity >= 0)
);

CREATE TABLE User (
    uid INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(30) UNIQUE,
    password VARCHAR(30),
    wallet DECIMAL(7, 2),
    CONSTRAINT chk_wallet CHECK (wallet >= 0),
    PRIMARY KEY (uid)
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


