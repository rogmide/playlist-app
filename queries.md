### Using the `movies_db` database, write the correct SQL queries for each of these tasks:

   #### 1.  The title of every movie.

	SELECT title from movies;

### 2.  All information on the G-rated movies.

	SELECT * from movies where rating = 'G';

### 3.  The title and release year of every movie, ordered with the oldest movie first.
    
	SELECT title, release_year from movies order BY release_year asc;
    
### 4.  All information on the 5 longest movies.

	SELECT * from movies order by runtime DESC limit 5;

### 5.  A query that returns the columns of `rating` and `total`, tabulating the total number of G, PG, PG-13, and R-rated movies.

	SELECT rating, count(rating) as total from movies group by rating;

### 6.  A table with columns of `release_year` and `average_runtime`, 	tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

	select release_year, round(avg(runtime), 0) as avg_runtime from movies group by release_year order by release_year desc;

### 7.  The movie title and studio name for every movie in the database.

	SELECT m.title, s.name from movies as m JOIN studios as s on m.studio_id = s.id;

### 8.  The star first name, star last name, and movie title for every matching movie and star pair in the database.

	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname, m.title 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id;

### 9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id 
	WHERE m.rating = 'G' 
	GROUP BY fullname;

### 10. The first and last names of every star along with the number of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure that two different actors with the same name are considered separately).

	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname, count(m.id) as total 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id 
	GROUP BY fullname 
	ORDER BY total desc;

## The rest of these are bonuses

### 11. The title of every movie along with the number of stars in that movie, in descending order by the number of stars.

	SELECT m.title, count(s.id) as casts 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id 
	GROUP BY m.title;

### 12. The first name, last name, and average runtime of the five stars whose movies have the longest average.

	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname, round(avg(m.runtime), 0)  as avg_runtime 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id 
	GROUP BY fullname 
	ORDER BY avg_runtime DESC 
	LIMIT 5;

### 13. The first name, last name, and average runtime of the five stars whose movies have the longest average, among stars who have more than one movie in the database.
	
	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname, round(avg(m.runtime), 0)  as avg_runtime 
	FROM stars as s 
	JOIN roles as r on s.id = r.star_id 
	JOIN movies as m on r.movie_id = m.id 
	GROUP BY fullname 
	HAVING count(m.id) > 1 
	ORDER BY avg_runtime desc 
	LIMIT 5;
	

### 14. The titles of all movies that don't feature any stars in our database.
	
	SELECT m.title 
	FROM movies as m 
	WHERE m.id 
	NOT IN (SELECT r.movie_id FROM roles as r)

### 15. The first and last names of all stars that don't appear in any movies in our database.
	
	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname 
	FROM stars as s 
	WHERE s.id 
	NOT IN (SELECT r.star_id from roles as r);

### 16. The first names, last names, and titles corresponding to every role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.

	SELECT CONCAT(s.first_name,' ', s.last_name) as fullname, m.title
	FROM stars as s 
	FULL join roles as r on s.id = r.star_id 
	FULL join movies as m on r.movie_id = m.id;
