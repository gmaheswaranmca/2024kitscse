sqlite:
    sofware: "DB Browser for SQLite"
--------------------------------------------------
SQL 
    - DDL - table,view,procedure,trigger
        CREATE TABLE    - table creation
        ALTER TABLE     - add columns, edit cols, add constraints
        DROP TABLE      - remove table from db 

        TRUCATE TABLE   - purge data, reset to struct  
    - DML   / DQL
        INSERT      - add row into table 
        UPDATE      - edit row 
        DELETE      - delete row 
        SELECT      - query ................
    - TCL (transaction - ACID)
        BEGIN TRANSACTION   - to let the db session bundle activies started 
        COMMIT              - to let db the activities shoud be updated to the db 
                                - completion 
        ROLLBACK            - reverse all the activies to previous state 
                                - rejection
        SAVEPOINT           - to set point from which we do commit / rollback 
    - DCL (data)
        GRANT 
            grant <privileges> on emp_db to 'user1'@'localhost';
                privileges: INSERT,UPDATE,DELETE,SELECT, 
                            CREATE,ALTER,DROP, GRANT 
        REVOKE 
            revoke <privileges> on emp_db from 'user1'@'localhost';  
--------------------------------------------------
dept: id, name  
    1 batting
    2 bowling
    3 wicket keeping 
emp: id, name, salary, dept_id, bonus 
         rohit, 100000, 1, 40000
         kohli, 125000, 1, 35000
         pant,  75000, 3, 55000
         surya, 120000, 1, 10000
         dube, 60000, 1, 20000
         pandiya, 95000, 2, 15000
         jadeja, 55000, 2, 20000
         axar, 70000, 2, 13000
         bumrah, 200000, 2, 75000
         arsheep, 75000, 2, 60000
         kuldeep, 50000, 2, 30000
--------------------------------------------------
CREATE TABLE dept (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) not null
);

INSERT INTO dept(name) 
	values('batting');
INSERT INTO dept(name) 
	values('bowling'),('wicket keeping');
	
DESC dept; -- not working

SELECT * FROM dept;

CREATE TABLE emp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) not null,
    salary FLOAT not null,
    dept_id INTEGER,
    bonus FLOAT not null,
	CONSTRAINT emp_dept_id_dept_id FOREIGN KEY(dept_id) REFERENCES dept(id)
);  

INSERT INTO emp(name, salary, dept_id, bonus)
    VALUES ('rohit', 100000, 1, 40000), ('kohli', 125000, 1, 35000),
         ('pant',  75000, 3, 55000),  ('surya', 120000, 1, 10000),
         ('dube', 60000, 1, 20000), ('pandiya', 95000, 2, 15000),
         ('jadeja', 55000, 2, 20000),('axar', 70000, 2, 13000),
         ('bumrah', 200000, 2, 75000),('arsheep', 75000, 2, 60000),
         ('kuldeep', 50000, 2, 30000);
		 
SELECT * FROM emp;		 
--------------------------------------------------       
24.06.2024
--------------------------------------------------
SELECT * FROM emp WHERE name='dube';

SELECT * FROM emp WHERE name='pandiya';

UPDATE emp
SET bonus = bonus + 20000
WHERE name='pandiya';

UPDATE emp
SET bonus = bonus + 5000
WHERE name='dube';
--------------------------------------------------
INSERT INTO emp(name, salary, dept_id, bonus)
    VALUES ('siraj', 80000, 2, 20000);

SELECT * FROM emp;

DELETE FROM emp WHERE name='siraj';
--------------------------------------------------
Queries:

Expressions and Filters 


SELECT * FROM dept;
SELECT * FROM emp;
-- display name and salary for all emps 
SELECT name, salary from emp;
-- display names who are getting salary above or equal 100000
SELECT name FROM emp where salary>=100000;
-- display name and total salary(salary+bonus) for all emps 
SELECT name, salary + bonus as total_salary from emp;
-- display name, salary, bonus, total_salary who are getting 
-- salary above or equal 100000
SELECT name, salary, bonus, 
   salary + bonus as total_salary
   FROM emp WHERE salary>=100000;
-- display player names who are batting dept
SELECT name FROM emp WHERE dept_id=1;
-- display player names who are bowling dept   
SELECT name FROM emp WHERE dept_id=2;
-- display player names who are wicket keeping dept   
SELECT name FROM emp WHERE dept_id=3;
-- display player names from either batting or 
-- wicket keeping dept
SELECT name FROM emp WHERE dept_id=1 OR dept_id=3;
SELECT name FROM emp WHERE dept_id IN (1,3);
-- display player names from neither batting nor 
-- wicket keeping dept
SELECT name FROM emp WHERE NOT(dept_id=1 OR dept_id=3);
SELECT name FROM emp WHERE dept_id NOT IN (1,3);

1. Display name, bonus, and bonus_percentage for bowlers using dept_id
SELECT name, bonus, ((bonus/salary)*100) as bonus_percentage
FROM emp WHERE dept_id=2;
2. Display name, salary, bonus, total_salary, bonus_percentage for batsmen using dept_id 
SELECT name, salary, bonus, 
    salary + bonus as total_salary, 
    ((bonus/salary)*100) as bonus_percentage
FROM emp WHERE dept_id=1;
3. Display name for bonus percentage less than 10%
SELECT name
FROM emp WHERE ((bonus/salary)*100)<10;
4. Display name for bonus percentage greater than 10%
SELECT name
FROM emp WHERE ((bonus/salary)*100)>10;
5. Display name, dept_id whose bonus above 15000
SELECT name, dept_id
FROM emp WHERE bonus>15000;

bonus_percentage = (bonus / salary) * 100
---------------------------------------------------------------------
Filters Operators 
    <   >    <>     =       <=      >=
    IN          BETWEEN         LIKE 

    Logical / Combination : AND     OR      NOT 
---------------------------------------------------------------------
-- Display names whose salary between 75000 and 100000
SELECT name FROM emp 
WHERE salary BETWEEN 75000 AND 100000;
-- 50000 and 74000
SELECT name FROM emp 
WHERE salary BETWEEN 50000 AND 74000;
-- not in the above range 
SELECT name FROM emp 
WHERE (salary NOT BETWEEN 75000 AND 100000) AND 
	(salary NOT BETWEEN 50000 AND 74000);
-- Display name and salary for batsman sort by salary ascending order 
SELECT name, salary 
FROM emp 
WHERE dept_id = 1 ORDER BY salary;   
--salary based Descending order 
SELECT name, salary 
FROM emp 
WHERE dept_id = 1 ORDER BY salary DESC;

-- display names starts with k 
select name from emp WHERE name like 'k%';

-- display names not starts with k 
select name from emp WHERE name not like 'k%';

-- display names ends with p 
select name from emp WHERE name like '%p';

--display names contains letter l
select name from emp WHERE name like '%l%';
---------------------------------------------------------------------
-- sub query 
-- display names whose dept name is 'batting' 
SELECT name FROM emp 
WHERE dept_id=(SELECT id FROM dept WHERE name='batting')
-- display names whose dept name is 'bowler' 
SELECT name FROM emp 
WHERE dept_id=(SELECT id FROM dept WHERE name='bowling')
-- aggregations 
-- find number of batsman 
SELECT count(*) as emp_count FROM emp where dept_id=1

-- find total salary of all bowlers 
SELECT sum(salary) as emp_count FROM emp where dept_id=2


-- find total salary of the company 
SELECT sum(salary) as tot_salary FROM emp


-- find avg salary of the company 
SELECT sum(salary)/count(*) as avg_salary FROM emp
SELECT avg(salary) as avg_salary FROM emp

-- find min salary and max salary of the bowling dept 
SELECT min(salary) as min_salary,
	max(salary) as max_salary 
FROM emp WHERE dept_id=2;

-- find the emp name of bowlind dept who is getting high pay 
SELECT name from emp 
where salary=(SELECT max(salary) from emp where dept_id=2)


-- group by, having 
"group by" will work along with aggregators 
- we classify the rows into groups 
- each group we target the aggregator 

-- distinct dept_ids, sorted 
SELECT dept_id
FROM emp 
GROUP BY dept_id 
-- find each dept total salary 
1 tot_sal 
2 tot_sal 
3 tot_sal
-- find each dept total salary
SELECT dept_id, sum(salary)
FROM emp 
GROUP BY dept_id 
-- find each dept min salary
SELECT dept_id, min(salary) as min_salary
FROM emp 
GROUP BY dept_id 
-- find each dept max salary
SELECT dept_id, max(salary) as max_salary
FROM emp 
GROUP BY dept_id 
-- find each dept avg salary
SELECT dept_id, avg(salary) as avg_salary
FROM emp 
GROUP BY dept_id 
-- find each dept num of employess
SELECT dept_id, count(*) as num_of_emp
FROM emp 
GROUP BY dept_id 

-- find each dept total salary - revisit 
SELECT dept_id, sum(salary) as total_salary
FROM emp 
GROUP BY dept_id 

-- find depts and total salary whose total salary > 400000
SELECT dept_id, sum(salary) as total_salary
FROM emp 
GROUP BY dept_id 
HAVING sum(salary)>400000



-- join 
---------------------------------------------------------------------
-- display emp name and dept name 
-- equi join 
SQL:
SELECT emp.name as emp_name,
    dept.name as dept_name 
FROM emp INNER JOIN dept 
    ON (emp.dept_id = dept.id)

-- cross join, each employee joins with each dept
SQL:
SELECT emp.name as emp_name,
    dept.name as dept_name 
FROM emp CROSS JOIN dept 


-- outer join
SQL: 
INSERT INTO dept(name) values('Impact');

-- joined rows + extra rows (non-joined rows) = outer join 
outer join concepts:
LEFT OUTER 
RIGHT OUTER 
FULL OUTER 

assumption is emp table has no foreign key, 
and has extra row(dept_id=6), 
its dept_id is not in the dept table 
12 emps, 4 depts 

emp INNER JOIN	dept ON (cond)! matched rows 
output: 11 rows 

emp LEFT OUTER JOIN	dept ON (cond)
! matched rows + extra rows in left table 
output: 11 rows, 1 extra row in emp table 
(here right side columns fields are null)  

emp RIGHT OUTER JOIN dept ON (cond)
! matched rows + extra rows in right table 
output: 11 rows, 1 extra row in dept table 
(here left side columns fields are null)  

emp FULL OUTER JOIN	dept ON (cond)
! matched rows + extra rows in left table 
			   + extra rows in right table 
output: 11 rows, 1 extra row in emp table,
(here dept columns fields are null)
		1 extra row in dept table 
(here emp columns fields are null)

-- emp_name, dept_name left outer join from dept
SQL:
SELECT emp.name as emp_name,
    dept.name as dept_name 
FROM dept LEFT OUTER JOIN emp
    ON (emp.dept_id = dept.id)

emp_name	dept_name
dube	batting
kohli	batting
rohit	batting
surya	batting
arsheep	bowling
axar	bowling
bumrah	bowling
jadeja	bowling
kuldeep	bowling
pandiya	bowling
pant	wicket keeping
null	Impact    

------------------------------------------------------------