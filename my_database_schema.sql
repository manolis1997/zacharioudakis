create database if not exists myproject;
use myproject;

create table anthropoi(
	id int not null auto_increment unique,
    fn varchar(40) not null,
    ln varchar(40) not null,
    age int not null,
    constraint pk1 primary key (id)

);


insert into anthropoi values(1,"manolis","zacharioudakis",24);
insert into anthropoi(fn,ln,age) values("paris","mavromatis",29);
insert into anthropoi(fn,ln,age) values("paris","maltezos",24);
insert into anthropoi(fn,ln,age) values("dimitris","georgakopoulos",22);
insert into anthropoi(fn,ln,age) values("mixalis","mixelakis",23);
insert into anthropoi(fn,ln,age) values("thodoris","platakos",24);
insert into anthropoi(fn,ln,age) values("dimitris","kourlos",25);
insert into anthropoi(fn,ln,age) values("stelios","stauroulakis",22);
insert into anthropoi(fn,ln,age) values("stavros","stavroulakis",23);
insert into anthropoi(fn,ln,age) values("markos","agas",27);


create table katagogi(
	id_kat int auto_increment unique not null,
    name varchar(40) not null default "athens",
    id_anth int not null,
    constraint pk_1 primary key (id_kat),
    constraint fk_1 foreign key (id_anth) references anthropoi(id)
);


INSERT INTO `myproject`.`katagogi`(`id_kat`,`name`,`id_anth`) VALUES (1000,"chania",1);
INSERT INTO `myproject`.`katagogi`(`id_anth`) VALUES (2);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("sparti",3);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("argos",4);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("chania",5);
INSERT INTO `myproject`.`katagogi`(`id_anth`) VALUES (6);
INSERT INTO `myproject`.`katagogi`(`id_anth`) VALUES (7);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("rethymno",8);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("rethymno",9);
INSERT INTO `myproject`.`katagogi`(`name`,`id_anth`) VALUES ("rethymno",10);

create table epaggelma(
    tomeas varchar(40),
    constraint p_k_2 primary key (tomeas)
);


insert into epaggelma values("idiotikos");
insert into epaggelma values("dimosios");

alter table anthropoi
add tomeas varchar(50);

alter table anthropoi
add constraint fk1 foreign key (tomeas)
references epaggelma(tomeas);


update anthropoi
set tomeas="idiotikos"
where age>=24;

update anthropoi
set tomeas="dimosios"
where age<24;

select * from anthropoi;
select * from epaggelma;
select * from katagogi;




