/* Feature 1 Index */
CREATE INDEX UserAuthIndex ON User(username)

/* Feature 2 Indices (Multiple needed since some fields can be blank) */
CREATE INDEX AllMovieFilterIndex ON Movie(title, rental_quantity, genre)
CREATE INDEX MovieTitleGenreIndex ON Movie(title, genre)
CREATE INDEX MovieQuantityGenreIndex ON Movie(rental_quantity, genre)
CREATE INDEX MovieGenreIndex ON Movie(genre)

/* No index needed for Feature 3 since there's automatically
an index on PK mid in Movie */

/* No index needed for Feature 4 since there's automatically
an index on PK (uid, mid) in Review */

/* No index needed for Feature 5 */

/* No index needed for Feature 6 */

/* Also we drop columns not needed before joining tables */
SELECT T.genre
FROM ((SELECT r.uid, r.mid FROM Rental r) NATURAL JOIN 
      (SELECT m.mid, m.genre Movie m)) AS T
WHERE T.uid = %s
