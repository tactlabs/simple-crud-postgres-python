# Simple CRUD PostgreSQL Python

<pre>
<code>
CREATE TABLE CITY (
	ID bigserial primary key,
   NAME varchar(20) NOT NULL,
	STATE varchar(20) NOT NULL,
	COUNTRY varchar(20) NOT NULL
);

INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Madurai', 'TA', 'India');
INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Theni', 'TA', 'India');

SELECT * FROM CITY;
</code>
</pre>

