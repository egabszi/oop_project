create table kosar_1 (
azonosito_1 int,
gyumolcs_1 varchar(20)
);


create table kosar_2 (
azonosito_2 int,
gyumolcs_2 varchar(20)
);



create table kosar_3 (
azonosito_3 int,
gyumolcs_3 varchar(20)
);

insert into kosar_1 (azonosito_1, gyumolcs_1) values 
(1, 'Alma'),
(2, 'Narancs'),
(3, 'Banán'),
(4, 'Paradicsom');


insert into kosar_2 (azonosito_2, gyumolcs_2) values 
(1, 'Narancs'),
(null, 'Alma'),
(3, null),
(4, 'Szilva');

insert into kosar_3
(azonosito_3, gyumolcs_3) values 
(1, 'asf'),
(2, 'asf'),
(3, 'af'),
(4, 'asf');



select * from kosar_1;
select * from kosar_2;

-- JOIN - táblák összekapcsolása
-- Közös metszet: Inner join
-- Left Join
-- Rigth Join
-- Full Join

--- (on - using)

select * from kosar_1 k1
inner join kosar_2 k2 on k1.gyumolcs_1 = k2.gyumolcs_2;


--- left join

select * from kosar_1 k1
left join kosar_2 k2 on k1.gyumolcs_1 = k2.gyumolcs_2
--where gyumolcs_2 is null
;

-- right join

select * from kosar_1 k1
right join kosar_2 k2 on k1.gyumolcs_1 = k2.gyumolcs_2


select * from kosar_1 k1
right join kosar_3 k3 on k1.gyumolcs_1 = k3.gyumolcs_3;

--

select * from kosar_1 k1
full outer join kosar_2 k2 on k1.gyumolcs_1 = k2.gyumolcs_2;


---constraintek - megszorítások

- valami ne legyen null érték -> muszáj, hogy kapjon értéket
- elsődleges kulcs leszel
- másodlagos kulcs - idegen kulcs - foreign key
........

create table test_car(
car_id int primary key,
name varchar(50) not null,
color varchar(10),
motor_type varchar(20),
price numeric
);

drop table test_car;
-- elsődleges kulcs - primary key
- ennek az értéke mindig egyedinek kell, hogy legyen
- ennek az értéke nem lehet null -> amikor létrehozom a táblában az adatot ,
  akkor minden esetben értéket kell neki adni
- létrejön egy unique index
- primary key azért is kellhet a táblára, ha szeretnénk foreing-key hivatkozásként használni


select * from test_car t where car_id = 2;

delete from test_car;

insert into test_car (car_id, name, color, motor_type, price) values (1, 'Zasztawa', 'Piros', 'Benzin', 10);
insert into test_car (car_id, name, color, motor_type, price) values (2, 'BMW', 'Fekete', 'Benzin', 100);
insert into test_car (car_id, name, color, motor_type, price) values (3, 'Merga', 'Fehér', 'Disel', 10);
insert into test_car (car_id, name, color, motor_type, price) values (4, 'Lada', 'Piros', 'Benzin', 1000);


create table test_car(
car_id int primary key,
name varchar(50) not null,
color varchar(10),
motor_type varchar(20),
price numeric
);

create table auto_bolt(
bolt_id serial primary key,
name varchar(50),
car_id int ,
  CONSTRAINT test_car_fk
      FOREIGN KEY(car_id) 
	  REFERENCES test_car(car_id)
	  ON DELETE CASCADE
);



insert into auto_bolt (name, car_id) values ('Stop shop', 2);

insert into auto_bolt (name, car_id) values ('Stop shop', 4);


select * from auto_bolt;

select * from test_car t where t.car_id = 2;


select
ab.bolt_id,
ab.name,
tc.car_id,
tc.name,
tc.color, 
tc.price
from auto_bolt ab
inner join test_car tc on ab.car_id = tc.car_id;

/*
 * 
 * select * from test_car t where t.name = 'BMW'
 * 
 * */

-- index segít  a következő műveleteknél: select (feltéve, hogy használod az indexet, 
--és az indexált mezőn nem végzel cast és egyégb műveletek) like '%a%'
-- lassít az index / indexek megléte: insert  - ETL, ELT 


