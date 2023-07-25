CREATE TABLE Movie (
    mid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    genre VARCHAR(30) NOT NULL,
    release_year INT NOT NULL, /* YYYY */
    duration INT NOT NULL, /* minutes */
    rental_price DECIMAL(5, 2) NOT NULL DEFAULT 9.99, /* Default price is $9.99 */
    rental_quantity INT NOT NULL DEFAULT 10,
    CONSTRAINT chk_rental_quantity CHECK (rental_quantity >= 0)
);

CREATE TABLE User (
    uid INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(30) NOT NULL,
    wallet DECIMAL(7, 2) NOT NULL DEFAULT 500.00,
    CONSTRAINT chk_wallet CHECK (wallet >= 0),
    PRIMARY KEY (uid)
);

CREATE TABLE Review (
    uid INT NOT NULL REFERENCES User(uid),
    mid INT NOT NULL REFERENCES Movie(mid),
    review_date DATE NOT NULL, /* 'YYYY-MM-DD' */
    rating INT NOT NULL CHECK(rating BETWEEN 1 and 5), /* Out of 5 stars */
    comment VARCHAR(500),
    PRIMARY KEY(uid, mid)
);

CREATE TABLE Rental (
    uid INT NOT NULL REFERENCES User(uid),
    mid INT NOT NULL REFERENCES Movie(mid),
    rent_date DATE NOT NULL, /* 'YYYY-MM-DD' */
    due_date DATE NOT NULL, /* Standard rent period is 2 weeks */
    is_active INT NOT NULL, /* 1 if rental is currently active, otherwise 0 */
    PRIMARY KEY(uid, mid, rent_date)
);


