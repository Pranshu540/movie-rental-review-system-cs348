CREATE TRIGGER DelUserReview AFTER DELETE ON user FOR EACH ROW DELETE FROM review WHERE uid = OLD.uid;

CREATE TRIGGER DelUserRental AFTER DELETE ON user FOR EACH ROW DELETE FROM rental WHERE uid = OLD.uid;

CREATE TRIGGER UpdateRentalQuantity AFTER DELETE ON rental FOR EACH ROW UPDATE movie SET rental_quantity = rental_quantity + 1 WHERE mid = OLD.mid AND OLD.is_active = 1;
