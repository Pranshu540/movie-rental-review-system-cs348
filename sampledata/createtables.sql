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

CREATE TABLE `Review` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `mid` int NOT NULL,
  `review_date` date NOT NULL,
  `rating` int NOT NULL,
  `comment` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`uid`,`mid`),
  CONSTRAINT `review_chk_1` CHECK ((`rating` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=9010 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `Rental` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `mid` int NOT NULL,
  `rent_date` date NOT NULL,
  `due_date` date NOT NULL,
  `is_active` int NOT NULL,
  PRIMARY KEY (`uid`,`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=2353400 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


