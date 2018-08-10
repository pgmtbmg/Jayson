PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE movie (id, title, origin, url, rating, image, directors, casts, year, genres, countries, summary);
COMMIT;
