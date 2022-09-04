SELECT * FROM movies;
SELECT * FROM studios;
SELECT * FROM stars;
SELECT * FROM roles;
-- ============================================================================= 
SELECT title FROM movies;
SELECT * FROM movies WHERE rating = 'G';
SELECT title, release_year FROM movies ORDER BY release_year ASC;
SELECT * FROM movies ORDER BY runtime DESC LIMIT 5;
SELECT rating, count(rating) AS total FROM movies GROUP BY rating;
SELECT release_year, round(avg(runtime), 0) AS avg_runtime FROM movies GROUP BY release_year ORDER BY release_year DESC;
SELECT m.title, s.name FROM movies AS m JOIN studios AS s ON m.studio_id = s.id;
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname, m.title FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id;
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id WHERE m.rating = 'G' GROUP BY fullname;
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname, count(m.id) AS total FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id GROUP BY fullname ORDER BY total DESC;
SELECT m.title, count(s.id) AS casts FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id GROUP BY m.title;
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname, round(avg(m.runtime), 0)  AS avg_runtime FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id GROUP BY fullname ORDER BY avg_runtime DESC LIMIT 5;
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname, round(avg(m.runtime), 0)  AS avg_runtime FROM stars AS s JOIN roles AS r ON s.id = r.star_id JOIN movies AS m ON r.movie_id = m.id GROUP BY fullname HAVING count(m.id) > 1 ORDER BY avg_runtime DESC LIMIT 5;
SELECT m.title FROM movies AS m WHERE m.id NOT IN (SELECT r.movie_id FROM roles AS r);
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname FROM stars AS s WHERE s.id NOT IN (SELECT r.star_id FROM roles AS r);
SELECT CONCAT(s.first_name,' ', s.last_name) AS fullname, m.title
FROM stars AS s 
FULL JOIN roles AS r ON s.id = r.star_id 
FULL JOIN movies AS m ON r.movie_id = m.id;

 


