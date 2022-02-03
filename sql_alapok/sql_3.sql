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


--delete 

delete from car where name='Nissan';

truncate table car;

-- ACID - Postgres tranzikójá az ACID -nak megfelelően kezeli.

a - atomicity - atomiság: garantálja, hogy a tranzakció az vagy (teljes egészében végbe megy) teljesül vagy nem
c - consistency - konzisztencia:
i - isolation - izoláció: 
d - durability - tartósság: tranzakció során keletkező változást azt valamilyen adattárolón kell tárolni,
hogy az esetleges hardveres, szoftveres és egyéb meghibásodás miatt ne legyen adatvesztés















