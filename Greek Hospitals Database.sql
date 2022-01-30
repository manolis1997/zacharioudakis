create database if not exists ygeia;
use ygeia;

create table asthenis(
id int auto_increment unique not null ,
f_n varchar(10) not null,
ln varchar(10) not null,
full_name varchar(25) as (concat(f_n," ",ln)),
im_eisagwghs date not null,
constraint pk1 primary key (id)
);

create table giatros(
id int auto_increment unique not null,
f_n varchar(20) not null,
l_n varchar(20) not null,
constraint pk_1 primary key(id)
);

alter table asthenis
add giatros int not null after im_eisagwghs;
alter table asthenis
add constraint fk1 foreign key (giatros) references giatros(id);

create table nosokomeio(
onoma varchar(30) unique not null,
perioxi varchar(30) not null,
constraint p_k_1 primary key (onoma)
);

alter table giatros
add douleia varchar(30) not null after l_n;
alter table giatros
add constraint f_k_1 foreign key (douleia) references nosokomeio(onoma);

alter table asthenis
add nosilia varchar(30) not null after giatros;
alter table asthenis
add constraint fk2 foreign key (nosilia) references nosokomeio(onoma);


insert into nosokomeio values ("euaggelismos","athina");
insert into nosokomeio values ("kratiko","athina");
insert into nosokomeio values ("ippokratio","thessaloniki");
insert into nosokomeio values ("papagewrgiou","thessaloniki");
insert into nosokomeio values ("lamias","lamia");
insert into nosokomeio values ("kumis","kumi");
insert into nosokomeio values ("xalkidas","xalkida");


insert into giatros(id,f_n,l_n,douleia) values(1,"manolis","zacharioudakis","kratiko");
insert into giatros(f_n,l_n,douleia) values("giannis","papadakis","ippokratio");
insert into giatros(f_n,l_n,douleia) values("manolis","mparadakis","euaggelismos");
insert into giatros(f_n,l_n,douleia) values("sakis","karagiorgas","lamias");
insert into giatros(f_n,l_n,douleia) values("alexandros","karathanos","kratiko");
insert into giatros(f_n,l_n,douleia) values("giorgos","kubelos","kratiko");
insert into giatros(f_n,l_n,douleia) values("panagiotis","mpakas","kratiko");
insert into giatros(f_n,l_n,douleia) values("giannis","athanasopoulos","euaggelismos");
insert into giatros(f_n,l_n,douleia) values("nikos","kafieris","ippokratio");
insert into giatros(f_n,l_n,douleia) values("argiris","kafritsas","lamias");
insert into giatros(f_n,l_n,douleia) values("stefanos","tzarimas","euaggelismos");

alter table asthenis
modify im_eisagwghs timestamp not null default CURRENT_TIMESTAMP;


insert into asthenis(id,f_n,ln,giatros,nosilia) values(100,"nikos","danikas",3,"ippokratio");
insert into asthenis(f_n,ln,im_eisagwghs,giatros,nosilia) values("nikos","mavrogenis","2022-01-20 10:33:21",5,"lamias");
insert into asthenis(f_n,ln,im_eisagwghs,giatros,nosilia) values("kostas","marantos","2021-12-22 09:21:10",6,"kratiko");
insert into asthenis(f_n,ln,giatros,nosilia) values("nikos","pappas",1,"kratiko");
insert into asthenis(f_n,ln,giatros,nosilia) values("james","gist",10,"euaggelismos");
insert into asthenis(f_n,ln,im_eisagwghs,giatros,nosilia) values("manolis","sifakis","2021-11-03 07:33:41",10,"euaggelismos");
insert into asthenis(f_n,ln,giatros,nosilia) values("makis","kourbelis",8,"kratiko");
insert into asthenis(f_n,ln,giatros,nosilia) values("spiros","risbanis",1,"kratiko");
insert into asthenis(f_n,ln,im_eisagwghs,giatros,nosilia) values("giannis","papandreou","2021-09-03 06:05:19",5,"lamias");
insert into asthenis(f_n,ln,im_eisagwghs,giatros,nosilia) values("thanasis","androutsos","2021-10-09 15:34:19",9,"kratiko");
insert into asthenis(f_n,ln,giatros,nosilia) values("giannis","dioudis",12,"lamias");

select * from asthenis;
select * from nosokomeio;
select * from giatros; 

/* Query about how many patients for each doctors*/
select g.l_n,count(*) as patients from asthenis a join giatros g on a.giatros=g.id group by g.id order by 1 desc;
/*	Query about how many doctors has each hospital*/
select g.l_n,n.onoma,count(*) from giatros g join nosokomeio n on g.douleia=n.onoma group by n.onoma;

/*General view of tables*/
select * from asthenis a join nosokomeio n on a.nosilia=n.onoma
						 join giatros g on a.giatros=g.id;

