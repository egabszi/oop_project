-- SQL - Structured Query Language - Szíkvel - SKÚL

-- objektumok

-- DML - Data Manupalution Language
-- insert , update, delete, merge (upsert) -> adat létrehozásra, törlése, változatásra, commit köteles műveletek

-- DDL - Data Definition Language
 --- create, drop, truncate, alter -y objektumokkal kapcsolatos műveltek: autocommitolnak

create table car(
name varchar(50),
color varchar(10),
motor_type varchar(20),
price numeric
);

-- * - minden mezőt a táblából
select * from car;
select name as "név", motor_type as "Motor típus", price as "összeg" from car; 
-- alias 

select c.name, c.motor_type, c.price from car c;

-- insert szintaktikája

insert into car (name, color, price) values ('Nissan', 'Fekete', 0);

-- OLTP  - On Line Transational Processing
--valahol van egy / több file-od

-- óva intelek titeket: 
-- nem írunk úgy insertet, hogy nem soroljuk fel a selectben a mezőket
insert into car
select * from car;

--- ezt szokjátok meg
insert into car (name, color, motor_type, price)
select name, color, motor_type, price from car;

update car set price = price * 0.5 where name = 'Volvo';

-- where clause

select * from car t
where name = 'Volvo'
or color = 'Fekete';

-- delete, update, select

-- követekező: delete 
-- indexekről
-- constraintek -> foreing key és primary_key

pcycopg -> natív sql-eket fogunk futtatni
