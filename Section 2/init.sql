create database salesdb;

\c salesdb;

create table manufacturer(
manufactureid int generated always as identity,
manufacturename text not null,
manufactureraddress char(100),
primary key(manufactureid)
)

create table cardetails(
carmodelid int generated always as identity,
carmodelname text not null,
manufactureid int not null,
releaseyear char(100),
weight float not null,
price float not null, 
constraint fk_manufacturer
foreign key(manufactureid) 
references manufacturer(manufactureid),
primary key(carmodelid)
)

create table client(
clientid int generated always as identity,
clientname text not null,
clientemail char(100) not null,
clientphone char(100) not null,
primary key(clientid)
)

create table salesperson(
salespersonid int generated always as identity,
salespersonname text not null,
salespersonemail char(100) not null,
salespersonphone char(100) not null,
primary key(salespersonid)
)

create table carsales(
id int generated always as identity,
salesdate date not null,
salestime time not null,
clientid int not null,
carmodelid int not null,
carserialno char(100),
salespersonid int not null, 
constraint fk_client
foreign key(clientid) 
references client(clientid),
constraint fk_salesperson
foreign key(salespersonid) 
references salesperson(salespersonid),
constraint fk_carmodel
foreign key(carmodelid) 
references cardetails(carmodelid)
) partition by range (salesdate);

insert into manufacturer(manufacturename,manufactureraddress) values ('Tesla','Singapore');
insert into manufacturer(manufacturename,manufactureraddress) values ('Audi','Singapore');




