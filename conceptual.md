### Conceptual Exercise

Answer the following questions below:

- ## What is PostgreSQL?

	**PostgreSQL** is an advanced, enterprise-class, and open-source relational database system.    PostgreSQL supports both SQL (relational) and JSON (non-relational) querying.

  
- ## What is the difference between SQL and PostgreSQL?

	
	### Some difference between the two.
	 

   ### PostgreSQL
	
	> PL/pgSQL procedural programming language
	
	> Scans the tables of a data layer to look for empty rows and gets rid of unnecessary elements.

	> Supports index-based table organization

	> Has well-developed multi-version concurrency control (MVCC) to tackle multiple procedures at the same time.

	> Is written in C language, and MS SQL is written in C and C++. In terms of language binding, PostgreSQL is very easy to use and connect to because of its external API
 		
	### SQL

	>Includes various high availability tools such as log shipping, failover clusters, and replication.

	>Uses T-SQL, which bears resemblance to standard SQL. T-SQL includes additional support for data and string processing, procedural programming, and local variables.

	>Provides an efficient garbage collector that doesn’t generate more than 15-20% of overhead.
	
	>Provides rich automated functionality for index management. They can be organized in clusters and sustain the proper row order without manual involvement.

	> Has a less developed multi-version concurrency control system and depends on locking of data to avoid errors from simultaneous transactions, by default.
		

- ## In `psql`, how do you connect to a database?
	
	 	psql: \c "db_name"
		

- ## What is the difference between `HAVING` and `WHERE`?

	| WHERE                            | HAVING                        |
	|:--------------------------------:|:-----------------------------:|
	| Filter records from the table for specified condition. | Filter record from the groups with specified condition. |
	| Can be used without GROUP BY Clause | Cannot be used without GROUP BY Clause
	| Can be used with SELECT, UPDATE, DELETE statement. | Can only be used with SELECT statement.	
	| Used before GROUP BY Clause | used after GROUP BY Clause
	| Used with single row function like UPPER, LOWER etc. | Used with multiple row function like SUM, COUNT etc.			

- ## What is the difference between an `INNER` and `OUTER` join?

	### Inner Join:

	> Inner join is an operation that returns combined tuples between two or more tables where at least one attribute is in common. If there is no attribute in common between tables then it will return nothing. 
	
	### Outer Join:
	
	> It is a type of Join operation .Outer join is an operation that returns combined tuples from a specified table even if the join condition fails. There are three types of outer join.
	
	>	1. Left Outer Join
	>	2. Right Outer Join
 	>	3. Full Outer Join

	

- ## What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

	### Left Outer Join:

	-  Returns all the rows from the table on the left and columns of the table on the right is null padded. Left Outer Join retrieves all the rows from both the tables that satisfy the join condition along with the unmatched rows of the left table.
	
	### Right Outer Join:

	- Right Outer Join returns all the rows from the table on the right and columns of the table on the left is null padded. Right Outer Join retrieves all the rows from both the tables that satisfy the join condition along with the unmatched rows of the right table.

- ## What is an ORM? What do they do?

	> An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application

- ## What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

	> Regular HTTP request as in window.location.href = "index.html", it clears the current window and loads the server response into the window.
	
	> Ajax request, the current window/document is unaffected and client-side or back-end can examine the results of the request and do some logic (insert HTML dynamically into the page or  parse JSON, etc...).

- ## What is CSRF? What is the purpose of the CSRF token?

	> A CSRF (Cross Site Request Forgery) Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. 

 	> The tokens are generated and submitted by the server-side application in a subsequent HTTP request made by the client.

- ## What is the purpose of `form.hidden_tag()`?

	> The form.hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF (Cross Site Request Forgery) attacks.
