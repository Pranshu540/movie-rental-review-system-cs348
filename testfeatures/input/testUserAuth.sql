SELECT EXISTS(SELECT 1 FROM User WHERE username='movielover123' AND password=’Secret48!’);
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password=’userPassword’);
INSERT INTO Users(username, password) VALUES ('userName', 'userPassword')
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password=’userPassword’);